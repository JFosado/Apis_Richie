from sqlalchemy.orm import Session
from datetime import datetime
import models.puestos_departamentos as models
import schemas.puestos_departamentos as schemas

def get_puesto_departamento(db: Session, id: int):
    return db.query(models.PuestoDepartamento).filter(models.PuestoDepartamento.PuestoID == id).first()

def get_puesto_departamento_by_nombre(db: Session, nombre: str):
    return db.query(models.PuestoDepartamento).filter(models.PuestoDepartamento.Nombre == nombre).first()

def get_puestos_departamentos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.PuestoDepartamento).offset(skip).limit(limit).all()

def create_puesto_departamento(db: Session, puesto_departamento: schemas.PuestoDepartamentoCreate):
    db_puesto_departamento = models.PuestoDepartamento(
        Nombre=puesto_departamento.Nombre,
        Descripcion=puesto_departamento.Descripcion,
        Salario=puesto_departamento.Salario,
        Turno=puesto_departamento.Turno,
        Creado=puesto_departamento.Creado or datetime.utcnow(),
        Modificado=puesto_departamento.Modificado or datetime.utcnow(),
        DepartamentoID=puesto_departamento.DepartamentoID
    )
    db.add(db_puesto_departamento)
    db.commit()
    db.refresh(db_puesto_departamento)
    return db_puesto_departamento

def update_puesto_departamento(db: Session, id: int, puesto_departamento: schemas.PuestoDepartamentoUpdate):
    db_puesto_departamento = db.query(models.PuestoDepartamento).filter(models.PuestoDepartamento.PuestoID == id).first()
    if not db_puesto_departamento:
        return None
    update_data = puesto_departamento.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_puesto_departamento, key, value)
    db.commit()
    db.refresh(db_puesto_departamento)
    return db_puesto_departamento

def delete_puesto_departamento(db: Session, id: int):
    db_puesto_departamento = db.query(models.PuestoDepartamento).filter(models.PuestoDepartamento.PuestoID == id).first()
    if not db_puesto_departamento:
        return None
    db.delete(db_puesto_departamento)
    db.commit()
    return db_puesto_departamento
