from fastapi import APIRouter,HTTPException,Depends,Request
from sqlalchemy.orm import Session
from portadortoken import Portador
import crud.citas,config.db,schemas.citas,models.citas
from typing import List

cita = APIRouter()

models.citas.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@cita.get("/citaAll/", response_model=List[schemas.citas.Citas], tags=["Citas"] ,dependencies=[Depends(Portador())])
def read_citas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_cita= crud.citas.get_citas(db=db, skip=skip, limit=limit)
    return db_cita

@cita.post("/citaOne/{ID}", response_model=schemas.citas.Citas, tags=["Citas"] ,dependencies=[Depends(Portador())])
def read_cita(ID: int, db: Session = Depends(get_db)):
    db_cita= crud.citas.get_cita(db=db, ID=ID)
    if db_cita is None:
        raise HTTPException(status_code=404, detail="Cita not found")
    return db_cita

@cita.post("/citaCreate/", response_model=schemas.citas.Citas, tags=["Citas"])
def create_cita(cita: schemas.citas.CitasCreate, db: Session = Depends(get_db)):
    db_cita = crud.citas.get_cita(db, ID=cita.Persona_ID)
    if db_cita:
        raise HTTPException(status_code=400, detail="Cita existente intenta nuevamente")
    return crud.citas.create_cita(db=db, cita=cita)


@cita.put("/citaUpdate/{ID}",  response_model=schemas.citas.Citas, tags=["Citas"] ,dependencies=[Depends(Portador())])
def update_cita(ID: int, cita: schemas.citas.CitasUpdate, db: Session = Depends(get_db)):
    db_cita = crud.citas.update_cita(db = db, ID = ID, cita = cita)
    if db_cita is None:
        raise HTTPException(status_code=404, detail="Cita no existente, no esta actualizado")
    return db_cita

@cita.delete("/citaDelete/{ID}", response_model=schemas.citas.Citas, tags=["Citas"] ,dependencies=[Depends(Portador())])
def delete_cita(ID: int, db: Session = Depends(get_db)):
    db_cita = crud.citas.delete_cita(db = db, ID = ID)
    if db_cita is None:
        raise HTTPException(status_code=404, detail="Cita no existente, no se pudo eliminar")
    return db_cita