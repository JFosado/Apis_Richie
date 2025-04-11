"""Rutas protegidas para la relación usuarios-roles."""

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config import db as db_config
from crud import usersrols as crud_userrol
from models import usersrols as model_userrol
from schemas import usersrols as userrol_schema
from portadortoken import Portador

userrol_router = APIRouter()

model_userrol.Base.metadata.create_all(bind=db_config.engine)


def get_db():
    """Provee una sesión de base de datos."""
    database = db_config.SessionLocal()
    try:
        yield database
    finally:
        database.close()


@userrol_router.get(
    "/usersrols/",
    response_model=List[userrol_schema.UserRol],
    tags=["Usuarios Roles"],
    dependencies=[Depends(Portador())],
    summary="Listar asignaciones"
)
def read_usersrols(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Lista todas las asignaciones usuario-rol."""
    return crud_userrol.get_usersrols(db=db, skip=skip, limit=limit)


@userrol_router.get(
    "/userrol/{user_id}/{rol_id}",
    response_model=userrol_schema.UserRol,
    tags=["Usuarios Roles"],
    dependencies=[Depends(Portador())],
    summary="Consultar asignación"
)
def read_userrol(user_id: str, rol_id: str, db: Session = Depends(get_db)):
    """Consulta una asignación usuario-rol específica."""
    userrol = crud_userrol.get_userrol(db=db, user_id=user_id, rol_id=rol_id)
    if not userrol:
        raise HTTPException(status_code=404, detail="Asignación no encontrada")
    return userrol


@userrol_router.post(
    "/userrols/",
    response_model=userrol_schema.UserRol,
    tags=["Usuarios Roles"],
    dependencies=[Depends(Portador())],
    summary="Crear asignación"
)
def create_userrol(userrol: userrol_schema.UserRolCreate, db: Session = Depends(get_db)):
    """Crea una nueva asignación usuario-rol."""
    existing = crud_userrol.get_userrol(db=db, user_id=userrol.usuario_id, rol_id=userrol.rol_id)
    if existing:
        raise HTTPException(status_code=400, detail="Asignación ya existente")
    return crud_userrol.create_userrol(db=db, userrol=userrol)


@userrol_router.put(
    "/userrol/{user_id}/{rol_id}",
    response_model=userrol_schema.UserRol,
    tags=["Usuarios Roles"],
    dependencies=[Depends(Portador())],
    summary="Actualizar asignación"
)
def update_userrol(user_id: str, rol_id: str, userrol: userrol_schema.UserRolUpdate, db: Session = Depends(get_db)):
    """Actualiza una relación usuario-rol existente."""
    updated = crud_userrol.update_userrol(db=db, user_id=user_id, rol_id=rol_id, userrol=userrol)
    if not updated:
        raise HTTPException(status_code=404, detail="Asignación no actualizada")
    return updated


@userrol_router.delete(
    "/userrol/{user_id}/{rol_id}",
    response_model=userrol_schema.UserRol,
    tags=["Usuarios Roles"],
    dependencies=[Depends(Portador())],
    summary="Eliminar asignación"
)
def delete_userrol(user_id: str, rol_id: str, db: Session = Depends(get_db)):
    """Elimina una relación usuario-rol existente."""
    deleted = crud_userrol.delete_userrol(db=db, user_id=user_id, rol_id=rol_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Asignación no eliminada")
    return deleted

userrol = userrol_router