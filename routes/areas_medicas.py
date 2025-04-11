# pylint: disable=too-many-arguments, redefined-builtin
"""Rutas de FastAPI para gestionar las áreas médicas del sistema."""


from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.areas_medicas
import config.db
import schemas.areas_medicas
import models.areas_medicas
from portadortoken import Portador

area_medica = APIRouter()

# Crear las tablas si no existen
models.areas_medicas.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    """
    Dependencia para obtener una sesión de base de datos.
    """
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@area_medica.get(
    "/areas_medicas/",
    response_model=List[schemas.areas_medicas.AreaMedica],
    tags=["Áreas Médicas"],
    dependencies=[Depends(Portador())],
    summary="Listar áreas médicas",
    description="""
Devuelve una lista de todas las áreas médicas registradas en el sistema.

- Protegido por JWT.
- Puedes usar `skip` y `limit` para paginar resultados.
"""
)
def read_areas_medicas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Endpoint para obtener todas las áreas médicas (protegido).
    """
    return crud.areas_medicas.get_areas_medicas(db=db, skip=skip, limit=limit)


@area_medica.get(
    "/area_medica/{id}",
    response_model=schemas.areas_medicas.AreaMedica,
    tags=["Áreas Médicas"],
    dependencies=[Depends(Portador())],
    summary="Consultar área médica por ID",
    description="""
Obtiene los detalles de una área médica específica a partir de su ID.

- Requiere autenticación JWT.
- Retorna error 404 si el área médica no existe.
"""
)
def read_area_medica(id: str, db: Session = Depends(get_db)):
    """
    Endpoint para consultar un área médica por ID (protegido).
    """
    db_area = crud.areas_medicas.get_area_medica(db=db, id=id)
    if db_area is None:
        raise HTTPException(status_code=404, detail="Área médica no encontrada")
    return db_area


@area_medica.post(
    "/areas_medicas/",
    response_model=schemas.areas_medicas.AreaMedica,
    tags=["Áreas Médicas"],
    summary="Registrar área médica",
    description="""
Crea una nueva área médica en el sistema.

- No requiere autenticación.
- Valida que no exista otra área médica con el mismo nombre.
"""
)
def create_area_medica(
    area: schemas.areas_medicas.AreaMedicaCreate,
    db: Session = Depends(get_db)
):
    """
    Endpoint para crear un área médica (libre).
    """
    db_area = crud.areas_medicas.get_area_medica_by_nombre(db, nombre=area.Nombre)
    if db_area:
        raise HTTPException(status_code=400, detail="El nombre del área médica ya existe")
    return crud.areas_medicas.create_area_medica(db=db, area=area)


@area_medica.put(
    "/area_medica/{id}",
    response_model=schemas.areas_medicas.AreaMedica,
    tags=["Áreas Médicas"],
    dependencies=[Depends(Portador())],
    summary="Actualizar área médica",
    description="""
Actualiza los datos de una área médica existente en el sistema.

- Requiere token JWT.
- Retorna error 404 si el área médica no existe.
"""
)
def update_area_medica(
    id: str,
    area: schemas.areas_medicas.AreaMedicaUpdate,
    db: Session = Depends(get_db)
):
    """
    Endpoint para actualizar un área médica (protegido).
    """
    db_area = crud.areas_medicas.update_area_medica(db=db, id=id, area=area)
    if db_area is None:
        raise HTTPException(
            status_code=404,
            detail="Área médica no encontrada, no se pudo actualizar"
        )
    return db_area


@area_medica.delete(
    "/area_medica/{id}",
    response_model=schemas.areas_medicas.AreaMedica,
    tags=["Áreas Médicas"],
    dependencies=[Depends(Portador())],
    summary="Eliminar área médica",
    description="""
Elimina una área médica existente por su ID.

- Protegido por JWT.
- Retorna error 404 si el área médica no existe.
"""
)
def delete_area_medica(id: str, db: Session = Depends(get_db)):
    """
    Endpoint para eliminar un área médica (protegido).
    """
    db_area = crud.areas_medicas.delete_area_medica(db=db, id=id)
    if db_area is None:
        raise HTTPException(
            status_code=404,
            detail="Área médica no encontrada, no se pudo eliminar"
        )
    return db_area
