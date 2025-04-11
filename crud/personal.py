from sqlalchemy.orm import Session
from datetime import datetime
import models.personal as models
import schemas.personal as schemas

def get_personal(db: Session, personal_id: str):
    return db.query(models.Personal).filter(models.Personal.id == personal_id).first()

def get_personal_all(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Personal).offset(skip).limit(limit).all()

def create_personal(db: Session, personal: schemas.PersonalCreate):
    db_personal = models.Personal(**personal.dict())
    db.add(db_personal)
    db.commit()
    db.refresh(db_personal)
    return db_personal

def update_personal(db: Session, personal_id: str, personal_data: schemas.PersonalUpdate):
    db_personal = db.query(models.Personal).filter(models.Personal.id == personal_id).first()
    if db_personal:
        for key, value in personal_data.dict(exclude_unset=True).items():
            setattr(db_personal, key, value)
        db_personal.fecha_actualizacion = datetime.utcnow()
        db.commit()
        db.refresh(db_personal)
    return db_personal

def delete_personal(db: Session, personal_id: str):
    db_personal = db.query(models.Personal).filter(models.Personal.id == personal_id).first()
    if db_personal:
        db.delete(db_personal)
        db.commit()
    return db_personal
