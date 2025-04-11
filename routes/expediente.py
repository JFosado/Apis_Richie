"""Operaciones CRUD para la entidad Expediente."""

from datetime import datetime
from sqlalchemy.orm import Session
import models.expediente as models
import schemas.expediente as schemas


def get_expediente(db: Session, expediente_id: int):
    """Retorna un expediente por su ID."""
    return db.query(models.Expediente).filter(models.Expediente.ID == expediente_id).first()


def get_expedientes(db: Session, skip: int = 0, limit: int = 10):
    """Retorna una lista de expedientes con paginación."""
    return db.query(models.Expediente).offset(skip).limit(limit).all()


def create_expediente(db: Session, expediente: schemas.ExpedienteCreate):
    """Crea y guarda un nuevo expediente en la base de datos."""

    db_expediente = models.Expediente(
        Paciente_ID=expediente.Paciente_ID,
        Descripcion=expediente.Descripcion,
        Fecha_Creacion=datetime.utcnow(),
    )
    db.add(db_expediente)
    try:
        db.commit()
        db.refresh(db_expediente)
    except Exception as exc:
        db.rollback()
        raise exc
    return db_expediente


def update_expediente(db: Session, expediente_id: int, expediente: schemas.ExpedienteUpdate):
    """Actualiza los campos de un expediente existente."""
    db_expediente = db.query(models.Expediente).filter(models.Expediente.ID == expediente_id).first()
    if db_expediente:
        for key, value in expediente.model_dump(exclude_unset=True).items():
            if value is not None:
                setattr(db_expediente, key, value)
        db_expediente.Fecha_Actualizacion = datetime.utcnow()
        try:
            db.commit()
            db.refresh(db_expediente)
        except Exception as exc:
            db.rollback()
            raise exc
    return db_expediente


def delete_expediente(db: Session, expediente_id: int):
    """Elimina un expediente de la base de datos si existe."""
    db_expediente = db.query(models.Expediente).filter(models.Expediente.ID == expediente_id).first()
    if db_expediente:
        try:
            db.delete(db_expediente)
            db.commit()
        except Exception as exc:
            db.rollback()
            raise exc
    return db_expediente


"""Rutas para operaciones con expedientes."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import crud.expediente as crud
import schemas.expediente as schemas
from config.db import SessionLocal  # Asegúrate de que config.db esté correctamente configurado
from portadortoken import Portador  # Asegúrate de que Portador esté definido y accesible

# Cambia el nombre del router a expediente_router
expediente_router = APIRouter()


def get_db():
    """Obtiene una sesión de base de datos."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@expediente_router.get("/expedientes/", response_model=List[schemas.ExpedienteResponse], tags=["Expedientes"], dependencies=[Depends(Portador())])
def read_expedientes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Obtiene una lista de expedientes con paginación."""
    return crud.get_expedientes(db=db, skip=skip, limit=limit)


@expediente_router.get("/expedientes/{expediente_id}", response_model=schemas.ExpedienteResponse, tags=["Expedientes"], dependencies=[Depends(Portador())])
def read_expediente(expediente_id: int, db: Session = Depends(get_db)):
    """Obtiene un expediente por su ID."""
    expediente = crud.get_expediente(db=db, expediente_id=expediente_id)
    if expediente is None:
        raise HTTPException(status_code=404, detail="Expediente no encontrado")
    return expediente


@expediente_router.post("/expedientes/", response_model=schemas.ExpedienteResponse, tags=["Expedientes"])
def create_expediente(expediente: schemas.ExpedienteCreate, db: Session = Depends(get_db)):
    """Crea un nuevo expediente."""
    return crud.create_expediente(db=db, expediente=expediente)


@expediente_router.put("/expedientes/{expediente_id}", response_model=schemas.ExpedienteResponse, tags=["Expedientes"], dependencies=[Depends(Portador())])
def update_expediente(expediente_id: int, expediente: schemas.ExpedienteUpdate, db: Session = Depends(get_db)):
    """Actualiza un expediente existente."""
    updated_expediente = crud.update_expediente(db=db, expediente_id=expediente_id, expediente=expediente)
    if updated_expediente is None:
        raise HTTPException(status_code=404, detail="Expediente no encontrado")
    return updated_expediente


@expediente_router.delete("/expedientes/{expediente_id}", response_model=dict, tags=["Expedientes"], dependencies=[Depends(Portador())])
def delete_expediente(expediente_id: int, db: Session = Depends(get_db)):
    """Elimina un expediente por su ID."""
    deleted_expediente = crud.delete_expediente(db=db, expediente_id=expediente_id)
    if deleted_expediente is None:
        raise HTTPException(status_code=404, detail="Expediente no encontrado")
    return {"message": "Expediente eliminado correctamente"}
