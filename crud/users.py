"""DAO para la gestión de usuarios en la base de datos."""

from sqlalchemy.orm import Session
from models import users as user_model
from schemas import users as user_schema


def get_user(db: Session, user_id: str):
    """Retorna un usuario por su ID."""
    return db.query(user_model.User).filter(user_model.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    """Busca un usuario por su nombre de usuario."""
    return db.query(user_model.User).filter(user_model.User.nombre_usuario == username).first()


def get_user_by_email(db: Session, email: str):
    """Busca un usuario por su correo electrónico."""
    return db.query(user_model.User).filter(user_model.User.correo_electronico == email).first()


def get_user_by_credentials(db: Session, username: str, correo: str, telefono: str, password: str):
    """
    Busca un usuario por nombre de usuario, correo o teléfono, y contraseña.
    """
    return db.query(user_model.User).filter(
        (
            (user_model.User.nombre_usuario == username) |
            (user_model.User.correo_electronico == correo) |
            (user_model.User.numero_telefonico_movil == telefono)
        ),
        user_model.User.contrasena == password
    ).first()


def get_users(db: Session, skip: int = 0, limit: int = 10):
    """Retorna una lista de usuarios con paginación."""
    return db.query(user_model.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: user_schema.UserCreate):
    """Crea un nuevo usuario en la base de datos."""
    db_user = user_model.User(
        persona_id=user.persona_id,
        nombre_usuario=user.nombre_usuario,
        correo_electronico=user.correo_electronico,
        contrasena=user.contrasena,
        numero_telefonico_movil=user.numero_telefonico_movil,
        estatus=user.estatus,
        fecha_registro=user.fecha_registro,
        fecha_actualizacion=user.fecha_actualizacion
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: str, user: user_schema.UserUpdate):
    """Actualiza los datos de un usuario existente."""
    db_user = db.query(user_model.User).filter(user_model.User.id == user_id).first()
    if db_user:
        for field, value in user.model_dump(exclude_unset=True).items():
            setattr(db_user, field, value)
        db.commit()
        db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: str):
    """Elimina un usuario por ID."""
    db_user = db.query(user_model.User).filter(user_model.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user
