"""Rutas para la gestión de personas."""

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

import crud.persons as crud
import schemas.persons as schemas
from config.db import SessionLocal
from portadortoken import Portador

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/persons/", response_model=List[schemas.Person], tags=["Personas"], dependencies=[Depends(Portador())])
def read_persons(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_persons(db=db, skip=skip, limit=limit)


@router.get("/person/{id}", response_model=schemas.Person, tags=["Personas"], dependencies=[Depends(Portador())])
def read_person(id: int, db: Session = Depends(get_db)):
    db_person = crud.get_person(db=db, person_id=id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    return db_person


@router.post("/person/", response_model=schemas.Person, tags=["Personas"])
def create_person(person: schemas.PersonCreate, db: Session = Depends(get_db)):
    db_person = crud.get_person_by_nombre(db, nombre=person.Nombre)
    if db_person:
        raise HTTPException(status_code=400, detail="Usuario existente, intenta nuevamente")
    return crud.create_person(db=db, person=person)


@router.put("/person/{id}", response_model=schemas.Person, tags=["Personas"], dependencies=[Depends(Portador())])
def update_person(id: int, person: schemas.PersonUpdate, db: Session = Depends(get_db)):
    db_person = crud.update_person(db=db, person_id=id, person=person)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    return db_person


@router.delete("/person/{id}", response_model=schemas.Person, tags=["Personas"], dependencies=[Depends(Portador())])
def delete_person(id: int, db: Session = Depends(get_db)):
    db_person = crud.delete_person(db=db, person_id=id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    return db_person

persons_router = router
