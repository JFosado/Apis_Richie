
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from portadortoken import Portador
import crud.espacios as crud
import config.db
import schemas.espacios as schemas

espacio = APIRouter()

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@espacio.get(
    "/espacios/",
    response_model=List[schemas.EspacioResponse],
    tags=["Espacios"],
    dependencies=[Depends(Portador())],
)
def read_espacios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_espacios(db=db, skip=skip, limit=limit)

@espacio.get(
    "/espacios/{id}",
    response_model=schemas.EspacioResponse,
    tags=["Espacios"],
    dependencies=[Depends(Portador())],
)
def read_espacio(id: str, db: Session = Depends(get_db)):
    db_espacio = crud.get_espacio(db=db, espacio_id=id)
    if db_espacio is None:
        raise HTTPException(status_code=404, detail="Espacio no encontrado")
    return db_espacio

@espacio.post(
    "/espacios/",
    response_model=schemas.EspacioResponse,
    tags=["Espacios"]
)
def create_espacio(espacio_data: schemas.EspacioCreate, db: Session = Depends(get_db)):
    return crud.create_espacio(db=db, espacio=espacio_data)

@espacio.put(
    "/espacios/{id}",
    response_model=schemas.EspacioResponse,
    tags=["Espacios"],
    dependencies=[Depends(Portador())],
)
def update_espacio(id: str, espacio_data: schemas.EspacioUpdate, db: Session = Depends(get_db)):
    db_espacio = crud.update_espacio(db=db, espacio_id=id, espacio=espacio_data)
    if db_espacio is None:
        raise HTTPException(status_code=404, detail="Espacio no encontrado")
    return db_espacio

@espacio.delete(
    "/espacios/{id}",
    response_model=dict,
    tags=["Espacios"],
    dependencies=[Depends(Portador())],
)
def delete_espacio(id: str, db: Session = Depends(get_db)):
    db_espacio = crud.delete_espacio(db=db, espacio_id=id)
    if db_espacio is None:
        raise HTTPException(status_code=404, detail="Espacio no encontrado")
    return {"message": "Espacio eliminado correctamente"}
