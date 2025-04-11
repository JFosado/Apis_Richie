import models.receta
import schemas.receta
from sqlalchemy.orm import Session

def get_receta(db:Session, ID:int):
    return db.query(models.receta.Receta).filter(models.receta.Receta.ID == ID).first()

def get_receta_by_Nombre(db: Session, Nombre: str):
    return db.query(models.receta.Receta).filter(models.receta.Receta == Nombre).first()

def get_recetas(db: Session, skip:int=0,limit:int=10):
    return db.query(models.receta.Receta).offset(skip).limit(limit).all()

def create_receta(db: Session, receta:schemas.receta.RecetaCreate):
    db_receta = models.receta.Receta(Nombre=receta.Nombre,Fecha_Nacimiento=receta.Fecha_Nacimiento,Peso=receta.Peso,Talla=receta.Talla,Edad=receta.Edad,Presion_arterial=receta.Presion_arterial,Diagnostico=receta.Diagnostico,Prescripcion_Medica=receta.Prescripcion_Medica )
    db.add(db_receta)
    db.commit()
    db.refresh(db_receta)
    return db_receta

def update_receta(db: Session, ID: int, receta: schemas.receta.RecetaUpdate):
    db_receta = db.query(models.receta.Receta).filter(models.receta.Receta.ID == ID).first()
    if db_receta:
        for var, value in vars(receta).items():
            setattr(db_receta, var, value) if value else None
        db.commit()
        db.refresh(db_receta)
    return db_receta

def delete_receta(db: Session, ID: int):
    db_receta = db.query(models.receta.Receta).filter(models.receta.Receta.ID == ID).first()
    if  db_receta:
        db.delete(db_receta)
        db.commit()
    return db_receta

