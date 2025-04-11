from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import crud.rols, config.db, schemas.rols, models.rols
from typing import List
from jwt_config import solicita_token
from portadortoken import Portador

key = Fernet.generate_key()
f = Fernet(key)

rol = APIRouter()

models.rols.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🔹 Listar roles (PROTEGIDO)
@rol.get(
    "/rols/",
    response_model=List[schemas.rols.Rol],
    tags=["Roles"],
    dependencies=[Depends(Portador())],
    summary="Listar roles",
    description="""
Obtiene una lista paginada de todos los roles registrados en el sistema.

- Requiere autenticación por token JWT.
- Puedes usar `skip` para omitir registros y `limit` para definir cuántos mostrar.
"""
)
def read_rols(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_rols = crud.rols.get_rols(db=db, skip=skip, limit=limit)
    return db_rols

# 🔹 Consultar rol por ID (PROTEGIDO)
@rol.get(
    "/rol/{id}",
    response_model=schemas.rols.Rol,
    tags=["Roles"],
    dependencies=[Depends(Portador())],
    summary="Consultar rol por ID",
    description="""
Devuelve la información de un rol específico a partir de su ID.

- Protegido por JWT.
- Retorna error 404 si no se encuentra.
"""
)
def read_rol(id: str, db: Session = Depends(get_db)):
    db_rol = crud.rols.get_rol(db=db, id=id)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="Rol not found")
    return db_rol

# 🔹 Crear nuevo rol (PROTEGIDO)
@rol.post(
    "/rols/",
    response_model=schemas.rols.Rol,
    tags=["Roles"],
    dependencies=[Depends(Portador())],
    summary="Crear rol",
    description="""
Crea un nuevo rol en el sistema si no existe uno con el mismo nombre.

- Protegido por JWT.
- Retorna error 400 si el nombre del rol ya está en uso.
"""
)
def create_rol(rol: schemas.rols.RolCreate, db: Session = Depends(get_db)):
    db_rol = crud.rols.get_rol_by_nombre(db, nombre=rol.Nombre)
    if db_rol:
        raise HTTPException(status_code=400, detail="Rol existente intenta nuevamente")
    return crud.rols.create_rol(db=db, rol=rol)

# 🔹 Actualizar rol por ID (PROTEGIDO)
@rol.put(
    "/rol/{id}",
    response_model=schemas.rols.Rol,
    tags=["Roles"],
    dependencies=[Depends(Portador())],
    summary="Actualizar rol",
    description="""
Actualiza los datos de un rol existente.

- Protegido por JWT.
- Retorna error 404 si el rol no existe.
"""
)
def update_rol(id: str, rol: schemas.rols.RolUpdate, db: Session = Depends(get_db)):
    db_rol = crud.rols.update_rol(db=db, id=id, rol=rol)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="Usuario no existe, no actualizado")
    return db_rol

# 🔹 Eliminar rol por ID (PROTEGIDO)
@rol.delete(
    "/rol/{id}",
    response_model=schemas.rols.Rol,
    tags=["Roles"],
    dependencies=[Depends(Portador())],
    summary="Eliminar rol",
    description="""
Elimina un rol del sistema por su ID.

- Protegido por JWT.
- Retorna error 404 si no se encuentra.
"""
)
def delete_rol(id: str, db: Session = Depends(get_db)):
    db_rol = crud.rols.delete_rol(db=db, id=id)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="Usuario no existe, no se pudo eliminar")
    return db_rol
