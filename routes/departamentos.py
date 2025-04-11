from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

# 📁 Imports locales
import schemas.departamentos as schemas
import models.departamentos as models
import crud.departamentos as crud
import config.db
from portadortoken import Portador

# 🧭 Inicializa el router con prefijo y categoría para la documentación
departamentos = APIRouter(
    prefix="/departamentos",
    tags=["Departamentos"]
)

# 🔌 Dependencia para obtener la sesión de la base de datos
def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🔹 Obtener todos los departamentos (PROTEGIDO)
@departamentos.get(
    "/",
    response_model=List[schemas.Departamento],
    dependencies=[Depends(Portador())],
    summary="Listar departamentos",
    description="""
Devuelve una lista completa de todos los departamentos registrados en el sistema.

- Protegido por JWT.
"""
)
def get_departamentos(db: Session = Depends(get_db)):
    return crud.get_departamentos(db)

# 🔹 Obtener un departamento por ID (PROTEGIDO)
@departamentos.get(
    "/{id}",
    response_model=schemas.Departamento,
    dependencies=[Depends(Portador())],
    summary="Consultar departamento por ID",
    description="""
Devuelve los detalles de un departamento específico a partir de su ID.

- Requiere token JWT.
- Retorna error 404 si no existe.
"""
)
def get_departamento(id: str, db: Session = Depends(get_db)):
    departamento = crud.get_departamento(db, id)
    if departamento is None:
        raise HTTPException(status_code=404, detail="Departamento no encontrado")
    return departamento

# 🔹 Crear un nuevo departamento (LIBRE)
@departamentos.post(
    "/",
    response_model=schemas.Departamento,
    summary="Registrar nuevo departamento",
    description="""
Crea un nuevo departamento en el sistema.

- No requiere autenticación.
"""
)
def create_departamento(departamento: schemas.DepartamentoCreate, db: Session = Depends(get_db)):
    return crud.create_departamento(db, departamento)

# 🔹 Actualizar un departamento existente (PROTEGIDO)
@departamentos.put(
    "/{id}",
    response_model=schemas.Departamento,
    dependencies=[Depends(Portador())],
    summary="Actualizar departamento",
    description="""
Actualiza la información de un departamento existente.

- Protegido con JWT.
- Retorna error 404 si no se encuentra el departamento.
"""
)
def update_departamento(id: str, departamento_data: schemas.DepartamentoUpdate, db: Session = Depends(get_db)):
    db_departamento = crud.update_departamento(db, id, departamento_data)
    if db_departamento is None:
        raise HTTPException(status_code=404, detail="Departamento no encontrado")
    return db_departamento

# 🔹 Eliminar un departamento (PROTEGIDO)
@departamentos.delete(
    "/{id}",
    response_model=dict,
    dependencies=[Depends(Portador())],
    summary="Eliminar departamento",
    description="""
Elimina un departamento del sistema según su ID.

- Protegido con JWT.
- Retorna error 404 si el departamento no existe.
"""
)
def delete_departamento(id: str, db: Session = Depends(get_db)):
    db_departamento = crud.delete_departamento(db, id)
    if db_departamento is None:
        raise HTTPException(status_code=404, detail="Departamento no encontrado")
    return {"message": "Departamento eliminado correctamente"}
