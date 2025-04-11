import models.cirugias
import schemas.cirugias
from sqlalchemy.orm import Session

def get_cirugia(db: Session, id: int):
    return db.query(models.cirugias.Cirugia).filter(models.cirugias.Cirugia.ID == id).first()

def get_cirugia_by_nombre(db: Session, nombre: str):
    return db.query(models.cirugias.Cirugia).filter(models.cirugias.Cirugia.Nombre == nombre).first()

def get_cirugias(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.cirugias.Cirugia).offset(skip).limit(limit).all()

def create_cirugia(db: Session, cirugia: schemas.cirugias.CirugiaCreate):
    db_cirugia = models.cirugias.Cirugia(
        Paciente_ID=cirugia.Paciente_ID,
        Espacio_Medico_ID=cirugia.Espacio_Medico_ID,
        Tipo=cirugia.Tipo,
        Nombre=cirugia.Nombre,
        Descripcion=cirugia.Descripcion,
        Nivel_Urgencia=cirugia.Nivel_Urgencia,
        Horario=cirugia.Horario,
        Observaciones=cirugia.Observaciones,
        Valoracion_Medica=cirugia.Valoracion_Medica,
        Estatus=cirugia.Estatus,
        Consumible=cirugia.Consumible,
        Fecha_Registro=cirugia.Fecha_Registro,
        Fecha_Actualizacion=cirugia.Fecha_Actualizacion
    )
    db.add(db_cirugia)
    db.commit()
    db.refresh(db_cirugia)
    return db_cirugia

def update_cirugia(db: Session, id: int, cirugia: schemas.cirugias.CirugiaUpdate):
    db_cirugia = db.query(models.cirugias.Cirugia).filter(models.cirugias.Cirugia.ID == id).first()
    if db_cirugia:
        for var, value in vars(cirugia).items():
            setattr(db_cirugia, var, value) if value else None
        db.commit()
        db.refresh(db_cirugia)
    return db_cirugia

def delete_cirugia(db: Session, id: int):
    db_cirugia = db.query(models.cirugias.Cirugia).filter(models.cirugias.Cirugia.ID == id).first()
    if db_cirugia:
        db.delete(db_cirugia)
        db.commit()
    return db_cirugia
