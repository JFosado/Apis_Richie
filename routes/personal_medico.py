"""Rutas para el manejo del personal médico."""

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

import crud.personal_medico as crud
import schemas.personal_medico as schemas
from config.db import SessionLocal
from portadortoken import Portador

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get(
    "/personal_medico/",
    response_model=List[schemas.PersonalMedicoResponse],
    tags=["Personal Médico"],
    dependencies=[Depends(Portador())]
)
def read_all_personal_medico(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_all_personal_medico(db=db, skip=skip, limit=limit)


@router.post(
    "/personal_medico/",
    response_model=schemas.PersonalMedicoResponse,
    tags=["Personal Médico"]
)
def create_personal_medico(personal_medico: schemas.PersonalMedicoCreate, db: Session = Depends(get_db)):
    existing = crud.get_personal_medico_by_id(db, persona_id=personal_medico.Persona_ID)
    if existing:
        raise HTTPException(status_code=400, detail="Personal existente, intenta nuevamente")
    return crud.create_personal_medico(db=db, personal_medico=personal_medico)


@router.put(
    "/personal_medico/{persona_id}",
    response_model=schemas.PersonalMedicoResponse,
    tags=["Personal Médico"],
    dependencies=[Depends(Portador())]
)
def update_personal_medico(persona_id: int, personal_medico: schemas.PersonalMedicoUpdate, db: Session = Depends(get_db)):
    db_personal_medico = crud.update_personal_medico(db=db, persona_id=persona_id, personal_medico=personal_medico)
    if db_personal_medico is None:
        raise HTTPException(status_code=404, detail="Personal no existente, no está actualizado")
    return db_personal_medico


@router.delete(
    "/personal_medico/{persona_id}",
    response_model=schemas.PersonalMedicoResponse,
    tags=["Personal Médico"],
    dependencies=[Depends(Portador())]
)
def delete_personal_medico(persona_id: int, db: Session = Depends(get_db)):
    db_personal_medico = crud.delete_personal_medico(db=db, persona_id=persona_id)
    if db_personal_medico is None:
        raise HTTPException(status_code=404, detail="Personal médico no existe, no se pudo eliminar")
    return db_personal_medico
