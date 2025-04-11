"""Módulo CRUD para operaciones relacionadas con espacios físicos."""

from datetime import datetime
from sqlalchemy.orm import Session
import models.espacios as models
import schemas.espacios as schemas

def get_espacio(db: Session, espacio_id: str):
    """
    Retorna un espacio según su ID.

    Args:
        db (Session): Sesión de base de datos.
        espacio_id (str): ID del espacio.

    Returns:
        Espacio: Instancia encontrada o None.
    """
    return db.query(models.Espacio).filter(
        models.Espacio.id == espacio_id
    ).first()


def get_espacios(db: Session, skip: int = 0, limit: int = 10):
    """
    Retorna una lista de espacios con paginación.

    Args:
        db (Session): Sesión de base de datos.
        skip (int): Registros a omitir.
        limit (int): Número máximo de registros.

    Returns:
        List[Espacio]: Lista de espacios.
    """
    return db.query(models.Espacio).offset(skip).limit(limit).all()


def create_espacio(db: Session, espacio: schemas.EspacioCreate):
    """
    Crea y registra un nuevo espacio en la base de datos.

    Args:
        db (Session): Sesión de base de datos.
        espacio (EspacioCreate): Datos del nuevo espacio.

    Returns:
        Espacio: Instancia creada.
    """
    db_espacio = models.Espacio(
        tipo=espacio.tipo,
        nombre=espacio.nombre,
        departamento_id=espacio.departamento_id,
        estatus=espacio.estatus,
        capacidad=espacio.capacidad,
        espacio_superior_id=espacio.espacio_superior_id,
        fecha_registro=datetime.utcnow()
    )
    db.add(db_espacio)
    try:
        db.commit()
        db.refresh(db_espacio)
    except Exception as e:
        db.rollback()
        raise e
    return db_espacio


def update_espacio(db: Session, espacio_id: str, espacio: schemas.EspacioUpdate):
    """
    Actualiza los campos de un espacio existente.

    Args:
        db (Session): Sesión de base de datos.
        espacio_id (str): ID del espacio a modificar.
        espacio (EspacioUpdate): Datos a actualizar.

    Returns:
        Espacio: Instancia actualizada o None si no se encontró.
    """
    db_espacio = db.query(models.Espacio).filter(
        models.Espacio.id == espacio_id
    ).first()
    if db_espacio:
        for var, value in espacio.dict(exclude_unset=True).items():
            if value is not None:
                setattr(db_espacio, var, value)
        db_espacio.fecha_actualizacion = datetime.utcnow()
        try:
            db.commit()
            db.refresh(db_espacio)
        except Exception as e:
            db.rollback()
            raise e
    return db_espacio


def delete_espacio(db: Session, espacio_id: str):
    """
    Elimina un espacio de la base de datos si existe.

    Args:
        db (Session): Sesión de base de datos.
        espacio_id (str): ID del espacio a eliminar.

    Returns:
        Espacio: Instancia eliminada o None si no se encontró.
    """
    db_espacio = db.query(models.Espacio).filter(
        models.Espacio.id == espacio_id
    ).first()
    if db_espacio:
        try:
            db.delete(db_espacio)
            db.commit()
        except Exception as e:
            db.rollback()
            raise e
    return db_espacio
