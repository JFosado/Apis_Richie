"""Rutas para operaciones con pacientes."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import crud.paciente as crud
import schemas.paciente as schemas
from config.db import SessionLocal
from portadortoken import Portador

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/pacientes/", response_model=List[schemas.PacienteResponse], tags=["Pacientes"], dependencies=[Depends(Portador())])
def read_pacientes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_pacientes(db=db, skip=skip, limit=limit)


@router.get("/pacientes/{paciente_id}", response_model=schemas.PacienteResponse, tags=["Pacientes"], dependencies=[Depends(Portador())])
def read_paciente(paciente_id: int, db: Session = Depends(get_db)):
    db_paciente = crud.get_paciente(db=db, paciente_id=paciente_id)
    if db_paciente is None:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return db_paciente


@router.post("/pacientes/", response_model=schemas.PacienteResponse, tags=["Pacientes"])
def create_paciente(paciente: schemas.PacienteCreate, db: Session = Depends(get_db)):
    return crud.create_paciente(db=db, paciente=paciente)


@router.put("/pacientes/{paciente_id}", response_model=schemas.PacienteResponse, tags=["Pacientes"], dependencies=[Depends(Portador())])
def update_paciente(paciente_id: int, paciente: schemas.PacienteUpdate, db: Session = Depends(get_db)):
    db_paciente = crud.update_paciente(db=db, paciente_id=paciente_id, paciente=paciente)
    if db_paciente is None:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return db_paciente


@router.delete("/pacientes/{paciente_id}", response_model=dict, tags=["Pacientes"], dependencies=[Depends(Portador())])
def delete_paciente(paciente_id: int, db: Session = Depends(get_db)):
    db_paciente = crud.delete_paciente(db=db, paciente_id=paciente_id)
    if db_paciente is None:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return {"message": "Paciente eliminado correctamente"}
