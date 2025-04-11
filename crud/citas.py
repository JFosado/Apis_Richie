from datetime import datetime
from sqlalchemy.orm import Session
import models.citas as models
import schemas.citas as schemas


def get_cita(db: Session, cita_id: int):
    """Obtiene una cita por su ID."""
    return db.query(models.Cita).filter(models.Cita.ID == cita_id).first()


def get_citas(db: Session, skip: int = 0, limit: int = 10):
    """Obtiene todas las citas con paginación."""
    return db.query(models.Cita).offset(skip).limit(limit).all()


def create_cita(db: Session, cita: schemas.CitaCreate):
    """Crea y guarda una nueva cita médica."""
    db_cita = models.Cita(
        Persona_ID=cita.Persona_ID,
        Hora_Cita=cita.Hora_Cita,
        Telefono=cita.Telefono,
        Correo_Electronico=cita.Correo_Electronico,
        Motivo_Cita=cita.Motivo_Cita,
        Estatus=cita.Estatus,
        Fecha_Registro=datetime.utcnow(),
    )
    db.add(db_cita)
    try:
        db.commit()
        db.refresh(db_cita)
    except Exception as e:
        db.rollback()
        raise e
    return db_cita


def update_cita(db: Session, cita_id: int, cita: schemas.CitaUpdate):
    """Actualiza los campos de una cita existente."""
    db_cita = db.query(models.Cita).filter(models.Cita.ID == cita_id).first()
    if db_cita:
        for var, value in cita.model_dump(exclude_unset=True).items():
            if value is not None:
                setattr(db_cita, var, value)
        db_cita.Fecha_Actualizacion = datetime.utcnow()
        try:
            db.commit()
            db.refresh(db_cita)
        except Exception as e:
            db.rollback()
            raise e
    return db_cita


def delete_cita(db: Session, cita_id: int):
    """Elimina una cita de la base de datos si existe."""
    db_cita = db.query(models.Cita).filter(models.Cita.ID == cita_id).first()
    if db_cita:
        try:
            db.delete(db_cita)
            db.commit()
        except Exception as e:
            db.rollback()
            raise e
    return db_cita
