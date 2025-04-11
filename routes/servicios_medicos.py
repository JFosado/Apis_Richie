"""Rutas protegidas para Servicios Médicos."""

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import crud.servicios_medicos as crud
import schemas.servicios_medicos as schemas
from config.db import SessionLocal
from portadortoken import Portador

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/servicios_medicos/", response_model=List[schemas.ServiceMResponse], tags=["Servicios Médicos"], dependencies=[Depends(Portador())])
def read_services_m(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_services_m(db=db, skip=skip, limit=limit)


@router.get("/servicios_medicos/{id}", response_model=schemas.ServiceMResponse, tags=["Servicios Médicos"], dependencies=[Depends(Portador())])
def read_service_m(id: str, db: Session = Depends(get_db)):
    db_service = crud.get_service_m(db=db, service_id=id)
    if db_service is None:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return db_service


@router.post("/servicios_medicos/", response_model=schemas.ServiceMResponse, tags=["Servicios Médicos"], dependencies=[Depends(Portador())])
def create_service_m(service: schemas.ServiceMCreate, db: Session = Depends(get_db)):
    db_service = crud.get_service_m_by_nombre(db, nombre=service.nombre)
    if db_service:
        raise HTTPException(status_code=400, detail="Servicio ya registrado")
    return crud.create_service_m(db=db, service=service)


@router.put("/servicios_medicos/{id}", response_model=schemas.ServiceMResponse, tags=["Servicios Médicos"], dependencies=[Depends(Portador())])
def update_service_m(id: str, service: schemas.ServiceMUpdate, db: Session = Depends(get_db)):
    db_service = crud.update_service_m(db=db, service_id=id, service=service)
    if db_service is None:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return db_service


@router.delete("/servicios_medicos/{id}", response_model=schemas.ServiceMResponse, tags=["Servicios Médicos"], dependencies=[Depends(Portador())])
def delete_service_m(id: str, db: Session = Depends(get_db)):
    db_service = crud.delete_service_m(db=db, service_id=id)
    if db_service is None:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return db_service
serviceM = router
