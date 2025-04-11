import models.citas
import schemas.citas
from sqlalchemy.orm import Session
import models, schemas

def get_cita(db:Session, ID:int):
    return db.query(models.citas.Cita).filter(models.citas.Cita.ID == ID).first()

def get_citas(db: Session, skip:int=0,limit:int=10):
    return db.query(models.citas.Cita).offset(skip).limit(limit).all()

def create_cita(db: Session, cita:schemas.citas.CitasCreate):
    db_cita = models.citas.Cita(Persona_ID = cita.Persona_ID,Hora_Cita=cita.Hora_Cita,Telefono=cita.Telefono,Correo_Electronico=cita.Correo_Electronico,Motivo_Cita=cita.Motivo_Cita,Estatus=cita.Estatus )
    db.add(db_cita)
    db.commit()
    db.refresh(db_cita)
    return db_cita

def update_cita(db: Session, ID: int, cita: schemas.citas.CitasUpdate):
    db_cita = db.query(models.citas.Cita).filter(models.citas.Cita.ID == ID).first()
    if db_cita:
        for var, value in vars(cita).items():
            setattr(db_cita, var, value) if value else None
        db.commit()
        db.refresh(db_cita)
    return db_cita

def delete_cita(db: Session, ID: int):
    db_cita = db.query(models.citas.Cita).filter(models.citas.Cita.ID == ID).first()
    if  db_cita:
        db.delete(db_cita)
        db.commit()
    return db_cita

