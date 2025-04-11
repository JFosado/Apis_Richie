"""Módulo CRUD para manejar la relación entre servicios médicos y consumibles."""

from sqlalchemy.orm import Session
import models.servicios_medicos_consumibles
import schemas.servicios_medicos_consumibles

def get_by_id(db: Session, id: str): 
    return db.query(models.servicios_medicos_consumibles.ServiciosMedicosConsumibles).filter(
        models.servicios_medicos_consumibles.ServiciosMedicosConsumibles.id == id
    ).first()

def get_all(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.servicios_medicos_consumibles.ServiciosMedicosConsumibles).offset(
        skip
    ).limit(limit).all()

def create(db: Session, data: schemas.servicios_medicos_consumibles.ServiciosMedicosConsumiblesCreate):
    db_record = models.servicios_medicos_consumibles.ServiciosMedicosConsumibles(
        id_servicio=data.id_servicio,
        id_consumible=data.id_consumible,
        cantidad_usada=data.cantidad_usada,
        fecha_uso=data.fecha_uso,
        observaciones=data.observaciones
    )
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record 

def update(db: Session, id: str, data: schemas.servicios_medicos_consumibles.ServiciosMedicosConsumiblesUpdate):  # <- CAMBIO A str
    db_record = db.query(models.servicios_medicos_consumibles.ServiciosMedicosConsumibles).filter(
        models.servicios_medicos_consumibles.ServiciosMedicosConsumibles.id == id
    ).first()
    if db_record:
        for key, value in data.dict(exclude_unset=True).items():
            setattr(db_record, key, value)
        db.commit()
        db.refresh(db_record)
    return db_record

def delete(db: Session, id: str): 
    db_record = db.query(models.servicios_medicos_consumibles.ServiciosMedicosConsumibles).filter(
        models.servicios_medicos_consumibles.ServiciosMedicosConsumibles.id == id
    ).first()
    if db_record:
        db.delete(db_record)
        db.commit()
    return db_record
