"""DAO para la gestión de relaciones entre usuarios y roles."""

from sqlalchemy.orm import Session
from models import usersrols as userrol_model
from schemas import usersrols as userrol_schema


def get_userrol(db: Session, user_id: str, rol_id: str):
    """Retorna una relación usuario-rol específica por IDs."""
    return db.query(userrol_model.UserRol).filter(
        userrol_model.UserRol.usuario_id == user_id,
        userrol_model.UserRol.rol_id == rol_id
    ).first()


def get_usersrols(db: Session, skip: int = 0, limit: int = 10):
    """Retorna una lista paginada de relaciones usuario-rol."""
    return db.query(userrol_model.UserRol).offset(skip).limit(limit).all()


def create_userrol(db: Session, userrol: userrol_schema.UserRolCreate):
    """Crea una nueva asignación de un rol a un usuario."""
    db_userrol = userrol_model.UserRol(
        usuario_id=userrol.usuario_id,
        rol_id=userrol.rol_id,
        estatus=userrol.estatus,
        fecha_registro=userrol.fecha_registro,
        fecha_actualizacion=userrol.fecha_actualizacion
    )
    db.add(db_userrol)
    db.commit()
    db.refresh(db_userrol)
    return db_userrol


def update_userrol(db: Session, user_id: str, rol_id: str, userrol: userrol_schema.UserRolUpdate):
    """Actualiza los campos de una relación usuario-rol específica."""
    db_userrol = db.query(userrol_model.UserRol).filter(
        userrol_model.UserRol.usuario_id == user_id,
        userrol_model.UserRol.rol_id == rol_id
    ).first()
    if db_userrol:
        for key, value in userrol.model_dump(exclude_unset=True).items():
            setattr(db_userrol, key, value)
        db.commit()
        db.refresh(db_userrol)
    return db_userrol


def delete_userrol(db: Session, user_id: str, rol_id: str):
    """Elimina una relación entre un usuario y un rol si existe."""
    db_userrol = db.query(userrol_model.UserRol).filter(
        userrol_model.UserRol.usuario_id == user_id,
        userrol_model.UserRol.rol_id == rol_id
    ).first()
    if db_userrol:
        db.delete(db_userrol)
        db.commit()
    return db_userrol
