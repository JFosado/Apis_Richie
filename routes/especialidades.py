# routes/especialidades.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import config.db
from portadortoken import Portador

import schemas.especialidades as schemas
import crud.especialidades as crud

especialidades_router = APIRouter(
    prefix="/especialidades",
    tags=["Especialidades"]
)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@especialidades_router.get("/", response_model=List[schemas.Especialidad], dependencies=[Depends(Portador())])
def listar_especialidades(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_especialidades(db, skip=skip, limit=limit)

@especialidades_router.get("/{id}", response_model=schemas.Especialidad, dependencies=[Depends(Portador())])
def obtener_especialidad(id: str, db: Session = Depends(get_db)):
    esp = crud.get_especialidad(db, id)
    if not esp:
        raise HTTPException(status_code=404, detail="Especialidad no encontrada")
    return esp

@especialidades_router.post("/", response_model=schemas.Especialidad)
def crear_especialidad(especialidad: schemas.EspecialidadCreate, db: Session = Depends(get_db)):
    return crud.create_especialidad(db, especialidad)

@especialidades_router.put("/{id}", response_model=schemas.Especialidad, dependencies=[Depends(Portador())])
def actualizar_especialidad(id: str, especialidad: schemas.EspecialidadUpdate, db: Session = Depends(get_db)):
    db_esp = crud.update_especialidad(db, id, especialidad)
    if db_esp is None:
        raise HTTPException(status_code=404, detail="Especialidad no encontrada")
    return db_esp

@especialidades_router.delete("/{id}", response_model=dict, dependencies=[Depends(Portador())])
def eliminar_especialidad(id: str, db: Session = Depends(get_db)):
    db_esp = crud.delete_especialidad(db, id)
    if db_esp is None:
        raise HTTPException(status_code=404, detail="Especialidad no encontrada")
    return {"message": "Especialidad eliminada correctamente"}
