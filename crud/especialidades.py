# crud/especialidades.py

from sqlalchemy.orm import Session
import models.especialidades as models
import schemas.especialidades as schemas
from datetime import datetime

def get_especialidad(db: Session, especialidad_id: str):
    return db.query(models.Especialidad).filter(models.Especialidad.id == especialidad_id).first()

def get_especialidades(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Especialidad).offset(skip).limit(limit).all()

def create_especialidad(db: Session, especialidad: schemas.EspecialidadCreate):
    db_esp = models.Especialidad(**especialidad.dict())
    db.add(db_esp)
    db.commit()
    db.refresh(db_esp)
    return db_esp

def update_especialidad(db: Session, especialidad_id: str, especialidad_data: schemas.EspecialidadUpdate):
    db_esp = db.query(models.Especialidad).filter(models.Especialidad.id == especialidad_id).first()
    if db_esp:
        for key, value in especialidad_data.dict(exclude_unset=True).items():
            setattr(db_esp, key, value)
        db_esp.fecha_actualizacion = datetime.utcnow()
        db.commit()
        db.refresh(db_esp)
    return db_esp

def delete_especialidad(db: Session, especialidad_id: str):
    db_esp = db.query(models.Especialidad).filter(models.Especialidad.id == especialidad_id).first()
    if db_esp:
        db.delete(db_esp)
        db.commit()
    return db_esp
