from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import crud.cirugias, config.db, schemas.cirugias, models.cirugias
from jwt_config import solicita_token
from portadortoken import Portador

cirugia_router = APIRouter()

models.cirugias.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@cirugia_router.get("/cirugias/", response_model=List[schemas.cirugias.Cirugia], tags=["Cirugías"], dependencies=[Depends(Portador())])
def read_cirugias(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_cirugias = crud.cirugias.get_cirugias(db=db, skip=skip, limit=limit)
    return db_cirugias

@cirugia_router.get("/cirugia/{id}", response_model=schemas.cirugias.Cirugia, tags=["Cirugías"], dependencies=[Depends(Portador())])
def read_cirugia(id: int, db: Session = Depends(get_db)):
    db_cirugia = crud.cirugias.get_cirugia(db=db, id=id)
    if db_cirugia is None:
        raise HTTPException(status_code=404, detail="Cirugía no encontrada")
    return db_cirugia

@cirugia_router.post("/cirugias/", response_model=schemas.cirugias.Cirugia, tags=["Cirugías"])
def create_cirugia(cirugia: schemas.cirugias.CirugiaCreate, db: Session = Depends(get_db)):
    db_cirugia = crud.cirugias.get_cirugia_by_nombre(db, nombre=cirugia.Nombre)
    if db_cirugia:
        raise HTTPException(status_code=400, detail="Cirugía existente, intenta nuevamente")
    return crud.cirugias.create_cirugia(db=db, cirugia=cirugia)

@cirugia_router.put("/cirugia/{id}", response_model=schemas.cirugias.Cirugia, tags=["Cirugías"], dependencies=[Depends(Portador())])
def update_cirugia(id: int, cirugia: schemas.cirugias.CirugiaUpdate, db: Session = Depends(get_db)):
    db_cirugia = crud.cirugias.update_cirugia(db=db, id=id, cirugia=cirugia)
    if db_cirugia is None:
        raise HTTPException(status_code=404, detail="Cirugía no encontrada, no actualizada")
    return db_cirugia

@cirugia_router.delete("/cirugia/{id}", response_model=schemas.cirugias.Cirugia, tags=["Cirugías"], dependencies=[Depends(Portador())])
def delete_cirugia(id: int, db: Session = Depends(get_db)):
    db_cirugia = crud.cirugias.delete_cirugia(db=db, id=id)
    if db_cirugia is None:
        raise HTTPException(status_code=404, detail="Cirugía no encontrada, no se pudo eliminar")
    return db_cirugia
