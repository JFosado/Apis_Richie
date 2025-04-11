"""Módulo CRUD para operaciones con áreas médicas."""

from sqlalchemy.orm import Session
import models.areas_medicas
import schemas.areas_medicas

def get_area_medica(db: Session, id: str):  # pylint: disable=redefined-builtin
    """
    Obtiene un área médica específica por su ID.

    Args:
        db (Session): Sesión de base de datos.
        id (str): ID del área médica (UUID como string).

    Returns:
        AreaMedica: Instancia encontrada o None.
    """
    return db.query(models.areas_medicas.AreaMedica).filter(
        models.areas_medicas.AreaMedica.ID == id
    ).first()


def get_area_medica_by_nombre(db: Session, nombre: str):
    """
    Obtiene un área médica por su nombre.

    Args:
        db (Session): Sesión de base de datos.
        nombre (str): Nombre del área médica.

    Returns:
        AreaMedica: Instancia encontrada o None.
    """
    return db.query(models.areas_medicas.AreaMedica).filter(
        models.areas_medicas.AreaMedica.Nombre == nombre
    ).first()


def get_areas_medicas(db: Session, skip: int = 0, limit: int = 10):
    """
    Devuelve una lista paginada de áreas médicas.

    Args:
        db (Session): Sesión de base de datos.
        skip (int): Número de registros a omitir.
        limit (int): Máximo número de registros a retornar.

    Returns:
        List[AreaMedica]: Lista de instancias encontradas.
    """
    return db.query(models.areas_medicas.AreaMedica).offset(skip).limit(limit).all()


def create_area_medica(db: Session, area: schemas.areas_medicas.AreaMedicaCreate):
    """
    Crea una nueva área médica.

    Args:
        db (Session): Sesión de base de datos.
        area (AreaMedicaCreate): Datos de entrada.

    Returns:
        AreaMedica: Instancia creada.
    """
    db_area = models.areas_medicas.AreaMedica(
        Nombre=area.Nombre,
        Descripcion=area.Descripcion,
        Estatus=area.Estatus
    )
    db.add(db_area)
    db.commit()
    db.refresh(db_area)
    return db_area


def update_area_medica(db: Session, id: str, area: schemas.areas_medicas.AreaMedicaUpdate):  # pylint: disable=redefined-builtin
    """
    Actualiza una área médica existente.

    Args:
        db (Session): Sesión de base de datos.
        id (str): ID del área médica a actualizar.
        area (AreaMedicaUpdate): Datos nuevos a aplicar.

    Returns:
        AreaMedica: Instancia actualizada o None si no existe.
    """
    db_area = db.query(models.areas_medicas.AreaMedica).filter(
        models.areas_medicas.AreaMedica.ID == id
    ).first()
    if db_area:
        for key, value in area.dict(exclude_unset=True).items():
            setattr(db_area, key, value)
        db.commit()
        db.refresh(db_area)
    return db_area


def delete_area_medica(db: Session, id: str):  # pylint: disable=redefined-builtin
    """
    Elimina un área médica por su ID.

    Args:
        db (Session): Sesión de base de datos.
        id (str): ID del área médica a eliminar.

    Returns:
        AreaMedica: Instancia eliminada o None si no se encontró.
    """
    db_area = db.query(models.areas_medicas.AreaMedica).filter(
        models.areas_medicas.AreaMedica.ID == id
    ).first()
    if db_area:
        db.delete(db_area)
        db.commit()
    return db_area
