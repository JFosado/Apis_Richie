"""Módulo CRUD para operaciones relacionadas con personal médico."""

from datetime import datetime
from sqlalchemy.orm import Session
import models.personal_medico as models
import schemas.personal_medico as schemas


def get_personal_medico_by_id(db: Session, persona_id: int):
    """Obtiene un registro de personal médico por su ID de persona."""
    return db.query(models.PersonalMedico).filter(
        models.PersonalMedico.Persona_ID == persona_id
    ).first()


def get_all_personal_medico(db: Session, skip: int = 0, limit: int = 10):
    """Obtiene todos los registros de personal médico con paginación."""
    return db.query(models.PersonalMedico).offset(skip).limit(limit).all()


def create_personal_medico(db: Session, personal_medico: schemas.PersonalMedicoCreate):
    """Crea y guarda un nuevo registro de personal médico."""
    db_personal_medico = models.PersonalMedico(
        Persona_ID=personal_medico.Persona_ID,
        Departamento_ID=personal_medico.Departamento_ID,
        Cedula_Profesional=personal_medico.Cedula_Profesional,
        Tipo=personal_medico.Tipo,
        Especialidad=personal_medico.Especialidad,
        Fecha_Contratacion=personal_medico.Fecha_Contratacion,
        Fecha_Termino_Contrato=personal_medico.Fecha_Termino_Contrato,
        Salario=personal_medico.Salario,
        Estatus=personal_medico.Estatus,
        Fecha_Registro=datetime.utcnow(),
    )
    db.add(db_personal_medico)
    try:
        db.commit()
        db.refresh(db_personal_medico)
    except Exception as e:
        db.rollback()
        raise e
    return db_personal_medico


def update_personal_medico(db: Session, persona_id: int, personal_medico: schemas.PersonalMedicoUpdate):
    """Actualiza los campos de un registro de personal médico."""
    db_personal_medico = db.query(models.PersonalMedico).filter(
        models.PersonalMedico.Persona_ID == persona_id
    ).first()
    if db_personal_medico:
        for var, value in personal_medico.model_dump(exclude_unset=True).items():
            if value is not None:
                setattr(db_personal_medico, var, value)
        db_personal_medico.Fecha_Actualizacion = datetime.utcnow()
        try:
            db.commit()
            db.refresh(db_personal_medico)
        except Exception as e:
            db.rollback()
            raise e
    return db_personal_medico


def delete_personal_medico(db: Session, persona_id: int):
    """Elimina un registro de personal médico por su ID de persona."""
    db_personal_medico = db.query(models.PersonalMedico).filter(
        models.PersonalMedico.Persona_ID == persona_id
    ).first()
    if db_personal_medico:
        try:
            db.delete(db_personal_medico)
            db.commit()
        except Exception as e:
            db.rollback()
            raise e
    return db_personal_medico
