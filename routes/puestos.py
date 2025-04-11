# routes/puestos.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import config.db
from portadortoken import Portador

import schemas.puestos as schemas
import models.puestos as models
import crud.puestos as crud

puestos_router = APIRouter(
    prefix="/puestos",
    tags=["Puestos"]
)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@puestos_router.get("/", response_model=List[schemas.Puesto], dependencies=[Depends(Portador())])
def listar_puestos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_puestos(db, skip=skip, limit=limit)

@puestos_router.get("/{id}", response_model=schemas.Puesto, dependencies=[Depends(Portador())])
def obtener_puesto(id: str, db: Session = Depends(get_db)):  # ID como str
    puesto = crud.get_puesto(db, id)
    if not puesto:
        raise HTTPException(status_code=404, detail="Puesto no encontrado")
    return puesto

@puestos_router.post("/", response_model=schemas.Puesto)
def crear_puesto(puesto: schemas.PuestoCreate, db: Session = Depends(get_db)):
    return crud.create_puesto(db, puesto)

@puestos_router.put("/{id}", response_model=schemas.Puesto, dependencies=[Depends(Portador())])
def actualizar_puesto(id: str, puesto: schemas.PuestoUpdate, db: Session = Depends(get_db)):  # ID como str
    db_puesto = crud.update_puesto(db, id, puesto)
    if db_puesto is None:
        raise HTTPException(status_code=404, detail="Puesto no encontrado")
    return db_puesto

@puestos_router.delete("/{id}", response_model=dict, dependencies=[Depends(Portador())])
def eliminar_puesto(id: str, db: Session = Depends(get_db)):  # ID como str
    db_puesto = crud.delete_puesto(db, id)
    if db_puesto is None:
        raise HTTPException(status_code=404, detail="Puesto no encontrado")
    return {"message": "Puesto eliminado correctamente"}
