# crud/puestos.py

from sqlalchemy.orm import Session
import models.puestos as models
import schemas.puestos as schemas
from datetime import datetime

def get_puesto(db: Session, puesto_id: str):  # ID como str
    return db.query(models.Puesto).filter(models.Puesto.id == puesto_id).first()

def get_puestos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Puesto).offset(skip).limit(limit).all()

def create_puesto(db: Session, puesto: schemas.PuestoCreate):
    db_puesto = models.Puesto(**puesto.dict())
    db.add(db_puesto)
    db.commit()
    db.refresh(db_puesto)
    return db_puesto

def update_puesto(db: Session, puesto_id: str, puesto_data: schemas.PuestoUpdate):  # ID como str
    db_puesto = db.query(models.Puesto).filter(models.Puesto.id == puesto_id).first()
    if db_puesto:
        for key, value in puesto_data.dict(exclude_unset=True).items():
            setattr(db_puesto, key, value)
        db_puesto.fecha_actualizacion = datetime.utcnow()
        db.commit()
        db.refresh(db_puesto)
    return db_puesto

def delete_puesto(db: Session, puesto_id: str):  # ID como str
    db_puesto = db.query(models.Puesto).filter(models.Puesto.id == puesto_id).first()
    if db_puesto:
        db.delete(db_puesto)
        db.commit()
    return db_puesto
