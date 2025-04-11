from fastapi import APIRouter,HTTPException,Depends,Request
from sqlalchemy.orm import Session
from portadortoken import Portador
import crud.personal_medico, models.personal_medico, config.db, schemas.personal_medico
from typing import List

personal_medico = APIRouter()

models.personal_medico.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@personal_medico.get("/personal_medico/", response_model=List[schemas.personal_medico.PersonalMedico], tags=["Personal Médico"] ,dependencies=[Depends(Portador())])
def read_all_personal_medico(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_personal_medico = crud.personal_medico.get_all_personal_medico(db=db, skip=skip, limit=limit)
    return db_personal_medico


@personal_medico.post("/personal_medico/", response_model=schemas.personal_medico.PersonalMedico, tags=["Personal Médico"])
def create_personal_medico(personalMedico: schemas.personal_medico.PersonalMedicoCreate, db: Session = Depends(get_db)):
    db_personal_medico = crud.personal_medico.get_personalMedico_by_ID(db, Persona_ID = personalMedico.Persona_ID)
    if db_personal_medico:
        raise HTTPException(status_code=400, detail="Personal existente intenta nuevamente")
    return crud.personal_medico.create_personal_medico(db=db, personalMedico=personalMedico)

@personal_medico.put("/personal_medico/{ID}", response_model=schemas.personal_medico.PersonalMedico, tags=["Personal Médico"], dependencies=[Depends(Portador)])
def update_personal_medico(ID: int, personal_medico: schemas.personal_medico.PersonalMedicoUpdate, db: Session = Depends(get_db)):
    db_personal_medico = crud.personal_medico.update_personal_medico(db=db, Persona_ID=ID, personal_medico=personal_medico)
    if db_personal_medico is None:
        raise HTTPException(status_code=404, detail="Personal no existente, no está actualizado")
    return db_personal_medico

@personal_medico.delete("/personal_medico/{Persona_ID}",response_model=schemas.personal_medico.PersonalMedico, tags=["Personal Médico"] ,dependencies=[Depends(Portador())])
def delete_personal_medico(Persona_ID: int, db: Session = Depends(get_db)):
    db_personal_medico = crud.personal_medico.delete_personal_medico(db = db, Persona_ID = Persona_ID)
    if db_personal_medico is None:
        raise HTTPException(status_code=404, detail="Personal medico no existe, no se pudo eliminar")
    return db_personal_medico
