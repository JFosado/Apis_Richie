# crud/horarios.py

from sqlalchemy.orm import Session
import models.horarios as models
import schemas.horarios as schemas
from datetime import datetime

def get_horario(db: Session, horario_id: str):  # ID como str
    return db.query(models.Horario).filter(models.Horario.id == horario_id).first()

def get_horarios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Horario).offset(skip).limit(limit).all()

def create_horario(db: Session, horario: schemas.HorarioCreate):
    db_horario = models.Horario(**horario.dict())
    db.add(db_horario)
    db.commit()
    db.refresh(db_horario)
    return db_horario

def update_horario(db: Session, horario_id: str, horario_data: schemas.HorarioUpdate):  # ID como str
    db_horario = db.query(models.Horario).filter(models.Horario.id == horario_id).first()
    if db_horario:
        for key, value in horario_data.dict(exclude_unset=True).items():
            setattr(db_horario, key, value)
        db_horario.fecha_actualizacion = datetime.utcnow()
        db.commit()
        db.refresh(db_horario)
    return db_horario

def delete_horario(db: Session, horario_id: str):  # ID como str
    db_horario = db.query(models.Horario).filter(models.Horario.id == horario_id).first()
    if db_horario:
        db.delete(db_horario)
        db.commit()
    return db_horario
