from fastapi import APIRouter,HTTPException,Depends,Request
from sqlalchemy.orm import Session
import crud.receta
import models.receta
from portadortoken import Portador
import crud.receta,config.db,schemas.receta,models.receta
from typing import List

import schemas.receta

receta = APIRouter()

models.receta.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@receta.get("/recetaAll/", response_model=List[schemas.receta.Receta], tags=["RecetaMedica"] ,dependencies=[Depends(Portador())])
def read_receta(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_receta= crud.receta.get_recetas(db=db, skip=skip, limit=limit)
    return db_receta

@receta.post("/recetaOne/{ID}", response_model=schemas.receta.Receta, tags=["RecetaMedica"] ,dependencies=[Depends(Portador())])
def read_receta(ID: int, db: Session = Depends(get_db)):
    db_receta= crud.receta.get_receta(db=db, ID=ID)
    if db_receta is None:
        raise HTTPException(status_code=404, detail="Prescription not found")
    return db_receta

@receta.post("/recetaCreate/", response_model=schemas.receta.Receta, tags=["RecetaMedica"])
def create_receta(receta: schemas.receta.RecetaCreate, db: Session = Depends(get_db)):
    db_receta = crud.receta.get_receta_by_Nombre(db, Nombre=receta.Nombre)
    if db_receta:
        raise HTTPException(status_code=400, detail="Receta existente intenta nuevamente")
    return crud.receta.create_receta(db=db, receta=receta)

@receta.put("/recetaUpdate/{ID}", response_model=schemas.receta.Receta, tags=["RecetaMedica"] ,dependencies=[Depends(Portador())])
def update_receta(ID: int, receta: schemas.receta.RecetaUpdate, db: Session = Depends(get_db)):
    db_receta = crud.receta.update_receta(db = db, ID = ID, receta=receta)
    if db_receta is None:
        raise HTTPException(status_code=404, detail="Receta no existente, no esta actuaizado")
    return db_receta

@receta.delete("/recetaDelete/{ID}", response_model=schemas.receta.Receta, tags=["RecetaMedica"] ,dependencies=[Depends(Portador())])
def delete_receta(ID: int, db: Session = Depends(get_db)):
    db_receta = crud.receta.delete_receta(db = db, ID = ID)
    if db_receta is None:
        raise HTTPException(status_code=404, detail="Receta no existe, no se pudo eliminar")
    return db_receta