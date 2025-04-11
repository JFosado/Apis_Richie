"""Rutas para gestión de usuarios protegidas con JWT."""

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from config import db as db_config
from crud import users as crud_users
from models import users as model_users
from schemas import users as user_schema
from jwt_config import solicita_token
from portadortoken import Portador

users_router = APIRouter()

model_users.Base.metadata.create_all(bind=db_config.engine)


def get_db():
    """Provee una sesión de base de datos."""
    database = db_config.SessionLocal()
    try:
        yield database
    finally:
        database.close()


@users_router.post(
    "/users/",
    response_model=user_schema.User,
    tags=["Usuarios"],
    dependencies=[Depends(Portador())],
    summary="Crear usuario"
)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    """Crea un nuevo usuario si no existe el nombre."""
    existing_user = crud_users.get_user_by_username(db, username=user.nombre_usuario)
    if existing_user:
        raise HTTPException(status_code=400, detail="Usuario ya existe")
    return crud_users.create_user(db=db, user=user)


@users_router.post(
    "/login/",
    tags=["User Login"],
    summary="Iniciar sesión"
)
def read_credentials(user: user_schema.UserLogin, db: Session = Depends(get_db)):
    """Valida credenciales y retorna JWT si son válidas."""
    db_user = crud_users.get_user_by_credentials(
        db,
        username=user.nombre_usuario,
        correo=user.correo_electronico,
        telefono=user.numero_telefonico_movil,
        password=user.contrasena
    )
    if not db_user:
        return JSONResponse(content={"mensaje": "Acceso denegado"}, status_code=404)

    token = solicita_token(user.model_dump())
    return JSONResponse(content={"token": token}, status_code=200)


@users_router.get(
    "/users/",
    response_model=List[user_schema.User],
    tags=["Usuarios"],
    dependencies=[Depends(Portador())],
    summary="Listar usuarios"
)
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Devuelve lista paginada de usuarios."""
    return crud_users.get_users(db=db, skip=skip, limit=limit)


@users_router.get(
    "/user/{user_id}",
    response_model=user_schema.User,
    tags=["Usuarios"],
    dependencies=[Depends(Portador())],
    summary="Consultar usuario por ID"
)
def read_user(user_id: str, db: Session = Depends(get_db)):
    """Consulta un usuario por ID."""
    user = crud_users.get_user(db=db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user


@users_router.put(
    "/user/{user_id}",
    response_model=user_schema.User,
    tags=["Usuarios"],
    dependencies=[Depends(Portador())],
    summary="Actualizar usuario"
)
def update_user(user_id: str, user: user_schema.UserUpdate, db: Session = Depends(get_db)):
    """Actualiza los datos de un usuario existente."""
    updated = crud_users.update_user(db=db, user_id=user_id, user=user)
    if not updated:
        raise HTTPException(status_code=404, detail="Usuario no actualizado")
    return updated


@users_router.delete(
    "/user/{user_id}",
    response_model=user_schema.User,
    tags=["Usuarios"],
    dependencies=[Depends(Portador())],
    summary="Eliminar usuario"
)
def delete_user(user_id: str, db: Session = Depends(get_db)):
    """Elimina un usuario existente."""
    deleted = crud_users.delete_user(db=db, user_id=user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Usuario no eliminado")
    return deleted

users = users_router
