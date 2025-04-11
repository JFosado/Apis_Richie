from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

import crud.persons as crud
import config.db
import schemas.persons as schemas
import models.persons as models
from portadortoken import Portador

# 🚀 Inicializa el router
persons_router = APIRouter(tags=["Personas"])

# 📦 Asegura que la tabla se cree si no existe
models.Base.metadata.create_all(bind=config.db.engine)

# 🔌 Dependencia para obtener la sesión de base de datos
def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🔐 Obtener todas las personas (protegido)
@persons_router.get(
    "/persons/",
    response_model=List[schemas.Person],
    dependencies=[Depends(Portador())],
    summary="Listar personas registradas",
    description="Devuelve una lista paginada de todas las personas registradas en el sistema."
)
def read_persons(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_persons(db=db, skip=skip, limit=limit)

# 🔐 Consultar persona por ID (protegido)
@persons_router.get(
    "/person/{id}",
    response_model=schemas.Person,
    dependencies=[Depends(Portador())],
    summary="Consultar persona por ID",
    description="Devuelve la información de una persona específica por su ID."
)
def read_person(id: str, db: Session = Depends(get_db)):
    db_person = crud.get_person(db=db, id=id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    return db_person

# 🔐 Actualizar persona (protegido)
@persons_router.put(
    "/person/{id}",
    response_model=schemas.Person,
    dependencies=[Depends(Portador())],
    summary="Actualizar persona",
    description="Actualiza la información de una persona existente."
)
def update_person(id: str, person: schemas.PersonUpdate, db: Session = Depends(get_db)):
    db_person = crud.update_person(db=db, id=id, person=person)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Persona no existe, no actualizada")
    return db_person

# 🔐 Eliminar persona (protegido)
@persons_router.delete(
    "/person/{id}",
    response_model=schemas.Person,
    dependencies=[Depends(Portador())],
    summary="Eliminar persona",
    description="Elimina a una persona registrada por ID."
)
def delete_person(id: str, db: Session = Depends(get_db)):
    db_person = crud.delete_person(db=db, id=id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Persona no existe, no se pudo eliminar")
    return db_person

# ✅ Crear persona (libre, sin protección JWT)
@persons_router.post(
    "/person/",
    response_model=schemas.Person,
    summary="Crear persona",
    description="Registra una nueva persona en el sistema."
)
def create_person(person: schemas.PersonCreate, db: Session = Depends(get_db)):
    db_person = crud.get_person_by_nombre(db, person=person.Nombre)
    if db_person:
        raise HTTPException(status_code=400, detail="Persona ya registrada con ese nombre")
    return crud.create_person(db=db, person=person)
