from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from portadortoken import Portador
import crud.citas, config.db, schemas.citas, models.citas
from typing import List

cita = APIRouter()
models.citas.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@cita.get("/citaAll/", response_model=List[schemas.serviciosMedicos.citas.CitaResponse], tags=["Citas"], dependencies=[Depends(Portador())])
def read_citas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.citas.get_citas(db=db, skip=skip, limit=limit)

@cita.post("/citaOne/{ID}", response_model=schemas.serviciosMedicos.citas.CitaResponse, tags=["Citas"], dependencies=[Depends(Portador())])
def read_cita(ID: int, db: Session = Depends(get_db)):
    db_cita = crud.citas.get_cita(db=db, cita_id=ID)
    if db_cita is None:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return db_cita

@cita.post("/citaCreate/", response_model=schemas.serviciosMedicos.citas.CitaResponse, tags=["Citas"])
def create_cita(cita: schemas.serviciosMedicos.citas.CitaCreate, db: Session = Depends(get_db)):
    return crud.citas.create_cita(db=db, cita=cita)

@cita.put("/citaUpdate/{ID}", response_model=schemas.serviciosMedicos.citas.CitaResponse, tags=["Citas"], dependencies=[Depends(Portador())])
def update_cita(ID: int, cita: schemas.serviciosMedicos.citas.CitaUpdate, db: Session = Depends(get_db)):
    db_cita = crud.citas.update_cita(db=db, cita_id=ID, cita=cita)
    if db_cita is None:
        raise HTTPException(status_code=404, detail="Cita no existente")
    return db_cita

@cita.delete("/citaDelete/{ID}", response_model=schemas.serviciosMedicos.citas.CitaResponse, tags=["Citas"], dependencies=[Depends(Portador())])
def delete_cita(ID: int, db: Session = Depends(get_db)):
    db_cita = crud.citas.delete_cita(db=db, cita_id=ID)
    if db_cita is None:
        raise HTTPException(status_code=404, detail="Cita no existente")
    return db_cita