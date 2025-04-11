"""Módulo CRUD para operaciones relacionadas con consumibles médicos."""

from sqlalchemy.orm import Session
import models.consumibles
import schemas.consumibles
from uuid import UUID

def get_consumibles(db: Session, skip: int = 0, limit: int = 10):
    """
    Obtiene una lista paginada de consumibles.
    """
    return db.query(models.consumibles.Consumible).offset(skip).limit(limit).all()


def get_consumible(db: Session, id: UUID):  # Ajustado a UUID
    """
    Obtiene un consumible por su ID.
    """
    return db.query(models.consumibles.Consumible).filter(
        models.consumibles.Consumible.id == str(id)
    ).first()


def get_consumibles_by_nombre(db: Session, nombre: str):
    """
    Obtiene un consumible por su nombre.
    """
    return db.query(models.consumibles.Consumible).filter(
        models.consumibles.Consumible.nombre == nombre
    ).first()


def create_consumible(db: Session, consumible: schemas.consumibles.ConsumibleCreate):
    """
    Crea un nuevo consumible.
    """
    db_consumible = models.consumibles.Consumible(**consumible.model_dump())
    db.add(db_consumible)
    db.commit()
    db.refresh(db_consumible)
    return db_consumible


def update_consumible(
    db: Session, id: UUID, consumible: schemas.consumibles.ConsumibleUpdate
):
    """
    Actualiza un consumible existente.
    """
    db_consumible = db.query(models.consumibles.Consumible).filter(
        models.consumibles.Consumible.id == str(id)
    ).first()
    if db_consumible:
        for key, value in consumible.model_dump(exclude_unset=True).items():
            setattr(db_consumible, key, value)
        db.commit()
        db.refresh(db_consumible)
    return db_consumible


def delete_consumible(db: Session, id: UUID):
    """
    Elimina un consumible por su ID.
    """
    db_consumible = db.query(models.consumibles.Consumible).filter(
        models.consumibles.Consumible.id == str(id)
    ).first()
    if db_consumible:
        db.delete(db_consumible)
        db.commit()
    return db_consumible
