from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.servicios_medicos, config.db, schemas.servicios_medicos, models.servicios_medicos
from typing import List
from portadortoken import Portador  # 🔐 Protección JWT

serviceM = APIRouter()

models.servicios_medicos.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🔒 Rutas protegidas con JWT
@serviceM.get(
    "/servicios_medicos/",
    response_model=List[schemas.servicios_medicos.Service],
    tags=["Servicios Médicos"],
    dependencies=[Depends(Portador())],
    summary="Listar servicios médicos",
    description="""
Devuelve una lista paginada de todos los servicios médicos registrados.

- Protegido por token JWT.
- Puedes usar parámetros `skip` y `limit` para paginar resultados.
"""
)
def read_servicesM(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return crud.servicios_medicos.get_servicesM(db=db, skip=skip, limit=limit)

@serviceM.get(
    "/servicios_medicos/{id}",
    response_model=schemas.servicios_medicos.Service,
    tags=["Servicios Médicos"],
    dependencies=[Depends(Portador())],
    summary="Consultar servicio médico por ID",
    description="""
Obtiene los detalles de un servicio médico específico a partir de su ID.

- Retorna error 404 si el servicio no existe.
"""
)
def read_serviceM(id: str, db: Session = Depends(get_db)):
    db_serviceM = crud.servicios_medicos.get_serviceM(db=db, id=id)
    if db_serviceM is None:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return db_serviceM

@serviceM.post(
    "/servicios_medicos/",
    response_model=schemas.servicios_medicos.Service,
    tags=["Servicios Médicos"],
    dependencies=[Depends(Portador())],
    summary="Crear nuevo servicio médico",
    description="""
Registra un nuevo servicio médico en el sistema.

- Verifica que no exista un servicio con el mismo nombre.
- Retorna el servicio creado.
"""
)
def create_serviceM(service: schemas.servicios_medicos.ServiceMCreate, db: Session = Depends(get_db)):
    db_serviceM = crud.servicios_medicos.get_serviceM_by_nombre(db, nombre=service.nombre)
    if db_serviceM:
        raise HTTPException(status_code=400, detail="Servicio existente, intenta nuevamente")
    return crud.servicios_medicos.create_serviceM(db=db, service=service)

@serviceM.put(
    "/servicios_medicos/{id}",
    response_model=schemas.servicios_medicos.Service,
    tags=["Servicios Médicos"],
    dependencies=[Depends(Portador())],
    summary="Actualizar servicio médico",
    description="""
Actualiza los datos de un servicio médico existente por su ID.

- Retorna error 404 si el servicio no existe.
"""
)
def update_serviceM(id: str, service: schemas.servicios_medicos.ServiceMUpdate, db: Session = Depends(get_db)):
    db_serviceM = crud.servicios_medicos.update_serviceM(db=db, id=id, service=service)
    if db_serviceM is None:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return db_serviceM

@serviceM.delete(
    "/servicios_medicos/{id}",
    response_model=schemas.servicios_medicos.Service,
    tags=["Servicios Médicos"],
    dependencies=[Depends(Portador())],
    summary="Eliminar servicio médico",
    description="""
Elimina un servicio médico registrado según su ID.

- Retorna error 404 si el servicio no se encuentra.
"""
)
def delete_serviceM(id: str, db: Session = Depends(get_db)):
    db_serviceM = crud.servicios_medicos.delete_serviceM(db=db, id=id)
    if db_serviceM is None:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return db_serviceM
