
"""Operaciones CRUD para la entidad Expediente."""

from datetime import datetime
from sqlalchemy.orm import Session
import models.expediente as models
import schemas.expediente as schemas


def get_expediente(db: Session, expediente_id: int):
    """Retorna un expediente por su ID."""
    return db.query(models.Expediente).filter(models.Expediente.id_expediente == expediente_id).first()


def get_expedientes(db: Session, skip: int = 0, limit: int = 10):
    """Retorna una lista de expedientes con paginación."""
    return db.query(models.Expediente).offset(skip).limit(limit).all()


def create_expediente(db: Session, expediente: schemas.ExpedienteCreate):
    """Crea y guarda un nuevo expediente en la base de datos."""

    db_expediente = models.Expediente(
        id_paciente=expediente.id_paciente,
        id_medico_responsable=expediente.id_medico_responsable,
        antecedentes_personales=expediente.antecedentes_personales,
        antecedentes_familiares=expediente.antecedentes_familiares,
        alergias=expediente.alergias,
        vacunas=expediente.vacunas,
        habitos_tabaquismo=expediente.habitos_tabaquismo,
        habitos_alcohol=expediente.habitos_alcohol,
        habitos_drogas=expediente.habitos_drogas,
        actividad_fisica=expediente.actividad_fisica,
        fecha_creacion=datetime.utcnow(),
    )
    db.add(db_expediente)
    try:
        db.commit()
        db.refresh(db_expediente)
    except Exception as exc:
        db.rollback()
        raise exc
    return db_expediente


def update_expediente(db: Session, expediente_id: int, expediente: schemas.ExpedienteUpdate):
    """Actualiza los campos de un expediente existente."""
    db_expediente = db.query(models.Expediente).filter(models.Expediente.id_expediente == expediente_id).first()
    if db_expediente:
        for key, value in expediente.model_dump(exclude_unset=True).items():
            if value is not None:
                setattr(db_expediente, key, value)
        db_expediente.fecha_creacion = datetime.utcnow()
        try:
            db.commit()
            db.refresh(db_expediente)
        except Exception as exc:
            db.rollback()
            raise exc
    return db_expediente


def delete_expediente(db: Session, expediente_id: int):
    """Elimina un expediente de la base de datos si existe."""
    db_expediente = db.query(models.Expediente).filter(models.Expediente.id_expediente == expediente_id).first()
    if db_expediente:
        try:
            db.delete(db_expediente)
            db.commit()
        except Exception as exc:
            db.rollback()
            raise exc
    return db_expediente