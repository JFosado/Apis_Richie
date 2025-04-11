"""Rutas protegidas para la gestión de roles."""

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from jwt_config import solicita_token
from portadortoken import Portador
import crud.rols as crud
import schemas.rols as schemas
from config.db import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/rols/", response_model=List[schemas.Rol], tags=["Roles"], dependencies=[Depends(Portador())])
def read_rols(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_rols(db=db, skip=skip, limit=limit)


@router.get("/rol/{id}", response_model=schemas.Rol, tags=["Roles"], dependencies=[Depends(Portador())])
def read_rol(id: str, db: Session = Depends(get_db)):
    db_rol = crud.get_rol(db=db, rol_id=id)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return db_rol


@router.post("/rols/", response_model=schemas.Rol, tags=["Roles"], dependencies=[Depends(Portador())])
def create_rol(rol: schemas.RolCreate, db: Session = Depends(get_db)):
    db_rol = crud.get_rol_by_nombre(db, nombre=rol.Nombre)
    if db_rol:
        raise HTTPException(status_code=400, detail="El rol ya existe")
    return crud.create_rol(db=db, rol=rol)


@router.put("/rol/{id}", response_model=schemas.Rol, tags=["Roles"], dependencies=[Depends(Portador())])
def update_rol(id: str, rol: schemas.RolUpdate, db: Session = Depends(get_db)):
    db_rol = crud.update_rol(db=db, rol_id=id, rol=rol)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return db_rol


@router.delete("/rol/{id}", response_model=schemas.Rol, tags=["Roles"], dependencies=[Depends(Portador())])
def delete_rol(id: str, db: Session = Depends(get_db)):
    db_rol = crud.delete_rol(db=db, rol_id=id)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return db_rol

rol = router
