# routes/horarios.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import config.db
from portadortoken import Portador

import schemas.horarios as schemas
import models.horarios as models
import crud.horarios as crud

horarios_router = APIRouter(
    prefix="/horarios",
    tags=["Horarios"]
)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@horarios_router.get("/", response_model=List[schemas.Horario], dependencies=[Depends(Portador())])
def listar_horarios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_horarios(db, skip=skip, limit=limit)

@horarios_router.get("/{id}", response_model=schemas.Horario, dependencies=[Depends(Portador())])
def obtener_horario(id: str, db: Session = Depends(get_db)):  # ID como str
    horario = crud.get_horario(db, id)
    if not horario:
        raise HTTPException(status_code=404, detail="Horario no encontrado")
    return horario

@horarios_router.post("/", response_model=schemas.Horario)
def crear_horario(horario: schemas.HorarioCreate, db: Session = Depends(get_db)):
    return crud.create_horario(db, horario)

@horarios_router.put("/{id}", response_model=schemas.Horario, dependencies=[Depends(Portador())])
def actualizar_horario(id: str, horario: schemas.HorarioUpdate, db: Session = Depends(get_db)):  # ID como str
    db_horario = crud.update_horario(db, id, horario)
    if db_horario is None:
        raise HTTPException(status_code=404, detail="Horario no encontrado")
    return db_horario

@horarios_router.delete("/{id}", response_model=dict, dependencies=[Depends(Portador())])
def eliminar_horario(id: str, db: Session = Depends(get_db)):  # ID como str
    db_horario = crud.delete_horario(db, id)
    if db_horario is None:
        raise HTTPException(status_code=404, detail="Horario no encontrado")
    return {"message": "Horario eliminado correctamente"}
