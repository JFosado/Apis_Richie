# pylint: disable=too-many-arguments, redefined-builtin
"""Rutas de FastAPI para gestionar los consumibles médicos."""

from typing import List
from uuid import UUID
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from portadortoken import Portador
import crud.consumibles
import config.db
import schemas.consumibles
import models.consumibles

consumible = APIRouter()

# Crear tablas si no existen
models.consumibles.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    """
    Dependencia para obtener una sesión de base de datos.
    """
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@consumible.get(
    "/consumibles/",
    response_model=List[schemas.consumibles.Consumible],
    tags=["Consumibles"],
    dependencies=[Depends(Portador())],
    summary="Listar consumibles",
    description="""
Devuelve una lista paginada de todos los consumibles disponibles en inventario.

- Protegido por JWT.
- Puedes usar `skip` y `limit` para paginar resultados.
"""
)
def read_consumibles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.consumibles.get_consumibles(db=db, skip=skip, limit=limit)


@consumible.get(
    "/consumible/{id}",
    response_model=schemas.consumibles.Consumible,
    tags=["Consumibles"],
    dependencies=[Depends(Portador())],
    summary="Consultar consumible por ID",
    description="""
Obtiene los detalles de un consumible específico a partir de su ID.

- Requiere autenticación JWT.
- Retorna error 404 si no existe.
"""
)
def read_consumible(id: UUID, db: Session = Depends(get_db)):  # 🟢 Cambiado a UUID
    db_consumible = crud.consumibles.get_consumible(db=db, id=id)
    if db_consumible is None:
        raise HTTPException(status_code=404, detail="Consumible no encontrado")
    return db_consumible


@consumible.post(
    "/consumibles/",
    response_model=schemas.consumibles.Consumible,
    tags=["Consumibles"],
    summary="Registrar consumible",
    description="""
Crea un nuevo consumible en el sistema.

- No requiere autenticación.
- Valida que no exista otro con el mismo nombre.
"""
)
def create_consumible(
    consumible: schemas.consumibles.ConsumibleCreate,
    db: Session = Depends(get_db)
):
    db_consumible = crud.consumibles.get_consumibles_by_nombre(
        db, nombre=consumible.nombre
    )
    if db_consumible:
        raise HTTPException(
            status_code=400,
            detail="Consumible existente, intenta nuevamente"
        )
    return crud.consumibles.create_consumible(db=db, consumible=consumible)


@consumible.put(
    "/consumible/{id}",
    response_model=schemas.consumibles.Consumible,
    tags=["Consumibles"],
    dependencies=[Depends(Portador())],
    summary="Actualizar consumible",
    description="""
Actualiza la información de un consumible existente.

- Requiere token JWT.
- Retorna error 404 si el consumible no existe.
"""
)
def update_consumible(
    id: UUID,  # 🟢 Cambiado a UUID
    consumible: schemas.consumibles.ConsumibleUpdate,
    db: Session = Depends(get_db)
):
    db_consumible = crud.consumibles.update_consumible(
        db=db, id=id, consumible=consumible
    )
    if db_consumible is None:
        raise HTTPException(
            status_code=404,
            detail="Consumible no existente, no se actualizó"
        )
    return db_consumible


@consumible.delete(
    "/consumible/{id}",
    response_model=schemas.consumibles.Consumible,
    tags=["Consumibles"],
    dependencies=[Depends(Portador())],
    summary="Eliminar consumible",
    description="""
Elimina un consumible existente por su ID.

- Protegido por JWT.
- Retorna error 404 si el consumible no existe.
"""
)
def delete_consumible(id: UUID, db: Session = Depends(get_db)):  #  Cambiado a UUID
    db_consumible = crud.consumibles.delete_consumible(db=db, id=id)
    if db_consumible is None:
        raise HTTPException(
            status_code=404,
            detail="Consumible no existe, no se pudo eliminar"
        )
    return db_consumible
