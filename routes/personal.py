from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import config.db
from portadortoken import Portador

import schemas.personal as schemas
import crud.personal as crud

personal_router = APIRouter(
    prefix="/personal",
    tags=["Personal"]
)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@personal_router.get("/", response_model=List[schemas.Personal], dependencies=[Depends(Portador())])
def listar_personal(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_personal_all(db, skip=skip, limit=limit)

@personal_router.get("/{id}", response_model=schemas.Personal, dependencies=[Depends(Portador())])
def obtener_personal(id: str, db: Session = Depends(get_db)):
    personal = crud.get_personal(db, id)
    if not personal:
        raise HTTPException(status_code=404, detail="Personal no encontrado")
    return personal

@personal_router.post("/", response_model=schemas.Personal)
def crear_personal(personal: schemas.PersonalCreate, db: Session = Depends(get_db)):
    return crud.create_personal(db, personal)

@personal_router.put("/{id}", response_model=schemas.Personal, dependencies=[Depends(Portador())])
def actualizar_personal(id: str, personal: schemas.PersonalUpdate, db: Session = Depends(get_db)):
    db_personal = crud.update_personal(db, id, personal)
    if db_personal is None:
        raise HTTPException(status_code=404, detail="Personal no encontrado")
    return db_personal

@personal_router.delete("/{id}", response_model=dict, dependencies=[Depends(Portador())])
def eliminar_personal(id: str, db: Session = Depends(get_db)):
    db_personal = crud.delete_personal(db, id)
    if db_personal is None:
        raise HTTPException(status_code=404, detail="Personal no encontrado")
    return {"message": "Personal eliminado correctamente"}
