"""CRUD para operaciones relacionadas con servicios médicos."""

from datetime import datetime
from sqlalchemy.orm import Session
import models.servicios_medicos as models
import schemas.servicios_medicos as schemas


def get_service_m(db: Session, service_id: str):
    return db.query(models.ServiceM).filter(models.ServiceM.id == service_id).first()


def get_service_m_by_nombre(db: Session, nombre: str):
    return db.query(models.ServiceM).filter(models.ServiceM.nombre == nombre).first()


def get_services_m(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.ServiceM).offset(skip).limit(limit).all()


def create_service_m(db: Session, service: schemas.ServiceMCreate):
    db_service = models.ServiceM(
        nombre=service.nombre,
        descripcion=service.descripcion,
        observaciones=service.observaciones,
        costo_servicio=service.costo_servicio,
        fecha_registro=datetime.utcnow(),
    )
    db.add(db_service)
    try:
        db.commit()
        db.refresh(db_service)
    except Exception as exc:
        db.rollback()
        raise exc
    return db_service


def update_service_m(db: Session, service_id: str, service: schemas.ServiceMUpdate):
    db_service = db.query(models.ServiceM).filter(models.ServiceM.id == service_id).first()
    if db_service:
        for key, value in service.model_dump(exclude_unset=True).items():
            setattr(db_service, key, value)
        db_service.fecha_actualizacion = datetime.utcnow()
        try:
            db.commit()
            db.refresh(db_service)
        except Exception as exc:
            db.rollback()
            raise exc
    return db_service


def delete_service_m(db: Session, service_id: str):
    db_service = db.query(models.ServiceM).filter(models.ServiceM.id == service_id).first()
    if db_service:
        try:
            db.delete(db_service)
            db.commit()
        except Exception as exc:
            db.rollback()
            raise exc
    return db_service
