"""Operaciones CRUD para la entidad Paciente."""

from datetime import datetime
from sqlalchemy.orm import Session
import models.paciente as models
import schemas.paciente as schemas


def get_paciente(db: Session, paciente_id: int):
    """Retorna un paciente por su ID."""
    return db.query(models.Paciente).filter(models.Paciente.ID == paciente_id).first()


def get_pacientes(db: Session, skip: int = 0, limit: int = 10):
    """Retorna una lista de pacientes con paginación."""
    return db.query(models.Paciente).offset(skip).limit(limit).all()


def create_paciente(db: Session, paciente: schemas.PacienteCreate):
    """Crea y guarda un nuevo paciente en la base de datos."""

    existing = db.query(models.Paciente).filter(
        models.Paciente.Persona_ID == paciente.Persona_ID
    ).first()
    if existing:
        raise Exception("Ya existe un paciente con esta Persona_ID")

    db_paciente = models.Paciente(
        Persona_ID=paciente.Persona_ID,
        NSS=paciente.NSS,
        Tipo_de_seguro=paciente.Tipo_de_seguro,
        Fecha_ultima_cita=paciente.Fecha_ultima_cita,
        Estatus_Medico=paciente.Estatus_Medico,
        Estatus_vida=paciente.Estatus_vida,
        Estatus=paciente.Estatus,
        Fecha_Registro=datetime.utcnow(),
    )
    db.add(db_paciente)
    try:
        db.commit()
        db.refresh(db_paciente)
    except Exception as exc:
        db.rollback()
        raise exc
    return db_paciente


def update_paciente(db: Session, paciente_id: int, paciente: schemas.PacienteUpdate):
    """Actualiza los campos de un paciente existente."""
    db_paciente = db.query(models.Paciente).filter(models.Paciente.ID == paciente_id).first()
    if db_paciente:
        for key, value in paciente.model_dump(exclude_unset=True).items():
            if value is not None:
                setattr(db_paciente, key, value)
        db_paciente.Fecha_Actualizacion = datetime.utcnow()
        try:
            db.commit()
            db.refresh(db_paciente)
        except Exception as exc:
            db.rollback()
            raise exc
    return db_paciente


def delete_paciente(db: Session, paciente_id: int):
    """Elimina un paciente de la base de datos si existe."""
    db_paciente = db.query(models.Paciente).filter(models.Paciente.ID == paciente_id).first()
    if db_paciente:
        try:
            db.delete(db_paciente)
            db.commit()
        except Exception as exc:
            db.rollback()
            raise exc
    return db_paciente
