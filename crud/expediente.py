import models.expediente
import schemas.expediente
from sqlalchemy.orm import Session
from sqlalchemy.orm import Session
import models, schemas

def get_expediente(db:Session, ID:int):
    return db.query(models.expediente.Expediente).filter(models.expediente.Expediente.ID == ID).first()

def get_expedientes(db: Session, skip:int=0,limit:int=10):
    return db.query(models.expediente.Expediente).offset(skip).limit(limit).all()

def create_expediente(db: Session, expediente:schemas.expediente.ExpedienteCreate):
    db_exp = models.expediente.Expediente(Persona_ID = expediente.Persona_ID,Hora_Consulta=expediente.Hora_Consulta, Diagnostico=expediente.Diagnostico, Tratamiento_Relacionado=expediente.Tratamiento_Relacionado,Observaciones=expediente.Observaciones,Estatus=expediente.Estatus)
    db.add(db_exp)
    db.commit()
    db.refresh(db_exp)
    return db_exp

def update_expediente(db: Session, ID: int, exp: schemas.expediente.ExpedienteUpdate):
    db_exp = db.query(models.expediente.Expediente).filter(models.expediente.Expediente.ID == ID).first()
    if db_exp:
        for var, value in vars(exp).items():
            setattr(db_exp, var, value) if value else None
        db.commit()
        db.refresh(db_exp)
    return db_exp

def delete_expediente(db: Session, ID: int):
    db_exp = db.query(models.expediente.Expediente).filter(models.expediente.Expediente.ID == ID).first()
    if  db_exp:
        db.delete(db_exp)
        db.commit()
    return db_exp
