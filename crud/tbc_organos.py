from sqlalchemy.orm import Session
import models.tbc_organos as models
import schemas.tbc_organos as schemas

def get_organos(db: Session, skip: int = 0, limit: int = 50):
    return db.query(models.Organo).offset(skip).limit(limit).all()

def get_organo(db: Session, id: int):
    return db.query(models.Organo).filter(models.Organo.ID == id).first()

def get_organo_by_nombre(db: Session, nombre: str):
    return db.query(models.Organo).filter(models.Organo.Nombre == nombre).first()

def create_organo(db: Session, organo: schemas.OrganoCreate):
    db_organo = models.Organo(**organo.dict())
    db.add(db_organo)
    db.commit()
    db.refresh(db_organo)
    return db_organo

def update_organo(db: Session, id: int, organo: schemas.OrganoUpdate):
    db_organo = db.query(models.Organo).filter(models.Organo.ID == id).first()
    if db_organo:
        for key, value in organo.dict().items():
            setattr(db_organo, key, value)
        db.commit()
        db.refresh(db_organo)
    return db_organo

def delete_organo(db: Session, id: int):
    db_organo = db.query(models.Organo).filter(models.Organo.ID == id).first()
    if db_organo:
        db.delete(db_organo)
        db.commit()
    return db_organo
