from fastapi import APIRouter,HTTPException,Depends,Request
from sqlalchemy.orm import Session
from portadortoken import Portador
import crud.expediente,config.db,schemas.expediente,models.expediente
from typing import List

expediente = APIRouter()

models.expediente.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@expediente.get("/expedienteAll/", response_model=List[schemas.expediente.Expediente], tags=["Expediente"] ,dependencies=[Depends(Portador())])
def read_expediente(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_exp= crud.expediente.get_expedientes(db=db, skip=skip, limit=limit)
    return db_exp

@expediente.post("/expedienteOne/{ID}", response_model=schemas.expediente.Expediente, tags=["Expediente"] ,dependencies=[Depends(Portador())])
def read_expediente(ID: int, db: Session = Depends(get_db)):
    db_exp= crud.expediente.get_expediente(db=db, ID=ID)
    if db_exp is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return db_exp

@expediente.post("/expedienteCreate/", response_model=schemas.expediente.Expediente, tags=["Expediente"])
def create_expediente(expediente: schemas.expediente.ExpedienteCreate, db: Session = Depends(get_db)):
    db_exp = crud.expediente.get_expediente(db, ID=expediente.Persona_ID)
    if db_exp:
        raise HTTPException(status_code=400, detail="Expediente existente intenta nuevamente")
    return crud.expediente.create_expediente(db=db, expediente=expediente)

@expediente.put("/expedienteUpdate/{ID}", response_model=schemas.expediente.Expediente, tags=["Expediente"] ,dependencies=[Depends(Portador())])
def update_expediente(ID: int, expediente: schemas.expediente.ExpedienteUpdate, db: Session = Depends(get_db)):
    db_exp = crud.expediente.update_expediente(db = db, ID = ID, expediente = expediente)
    if db_exp is None:
        raise HTTPException(status_code=404, detail="Persona no existente, no esta actuaizado")
    return db_exp

@expediente.delete("/expedienteDelete/{ID}", response_model=schemas.expediente.Expediente, tags=["Expediente"] ,dependencies=[Depends(Portador())])
def delete_expediente(ID: int, db: Session = Depends(get_db)):
    db_exp = crud.expediente.delete_expediente(db = db, ID = ID)
    if db_exp is None:
        raise HTTPException(status_code=404, detail="Persona no existe, no se pudo eliminar")
    return db_exp