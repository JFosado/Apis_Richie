from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import crud.puestos_departamentos as crud_puestos_departamentos
import schemas.puestos_departamentos as schemas
import config.db
from jwt_config import solicita_token
from portadortoken import Portador
from models.puestos_departamentos import Base  # Asegúrate de importar Base desde el módulo correcto

puesto_departamento = APIRouter()

# Crea las tablas si no existen
Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@puesto_departamento.get("/puestos_departamentos/", response_model=List[schemas.PuestoDepartamento], tags=["Puestos Departamentos"], dependencies=[Depends(Portador())])
def read_puestos_departamentos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_puestos_departamentos.get_puestos_departamentos(db, skip, limit)

@puesto_departamento.get("/puesto_departamento/{id}", response_model=schemas.PuestoDepartamento, tags=["Puestos Departamentos"], dependencies=[Depends(Portador())])
def read_puesto_departamento(id: int, db: Session = Depends(get_db)):
    db_puesto_departamento = crud_puestos_departamentos.get_puesto_departamento(db, id)
    if db_puesto_departamento is None:
        raise HTTPException(status_code=404, detail="Puesto departamento no encontrado")
    return db_puesto_departamento

@puesto_departamento.post("/puestos_departamentos/", response_model=schemas.PuestoDepartamento, tags=["Puestos Departamentos"])
def create_puesto_departamento(puesto_departamento: schemas.PuestoDepartamentoCreate, db: Session = Depends(get_db)):
    return crud_puestos_departamentos.create_puesto_departamento(db, puesto_departamento)

@puesto_departamento.put("/puesto_departamento/{id}", response_model=schemas.PuestoDepartamento, tags=["Puestos Departamentos"], dependencies=[Depends(Portador())])
def update_puesto_departamento(id: int, puesto_departamento: schemas.PuestoDepartamentoUpdate, db: Session = Depends(get_db)):
    db_puesto_departamento = crud_puestos_departamentos.update_puesto_departamento(db, id, puesto_departamento)
    if db_puesto_departamento is None:
        raise HTTPException(status_code=404, detail="Puesto departamento no encontrado, no se pudo actualizar")
    return db_puesto_departamento

@puesto_departamento.delete("/puesto_departamento/{id}", response_model=schemas.PuestoDepartamento, tags=["Puestos Departamentos"], dependencies=[Depends(Portador())])
def delete_puesto_departamento(id: int, db: Session = Depends(get_db)):
    db_puesto_departamento = crud_puestos_departamentos.delete_puesto_departamento(db, id)
    if db_puesto_departamento is None:
        raise HTTPException(status_code=404, detail="Puesto departamento no encontrado, no se pudo eliminar")
    return db_puesto_departamento
