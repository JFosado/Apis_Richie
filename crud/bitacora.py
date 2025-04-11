from sqlalchemy.orm import Session
from models import bitacora as models_bitacora
from schemas import bitacora as schemas_bitacora

def get_bitacora(db: Session, id: int):
    return db.query(models_bitacora.Bitacora).filter(models_bitacora.Bitacora.ID == id).first()

def get_all_bitacora(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models_bitacora.Bitacora).offset(skip).limit(limit).all()

def get_role_by_bitacora(db: Session, nombre: str):
    return db.query(models_bitacora.Bitacora).filter(models_bitacora.Bitacora.Usuario == nombre).first()

def create_role(db: Session, bitacora: schemas_bitacora.BitacoraCreate):
    db_bitacora = models_bitacora.Bitacora(
        Usuario=bitacora.Usuario,
        Operacion=bitacora.Operacion,
        Tabla=bitacora.Tabla,
        Descripcion=bitacora.Descripcion,
        Estatus=bitacora.Estatus,
        Fecha_Registro=bitacora.Fecha_Registro
    )
    db.add(db_bitacora)
    db.commit()
    db.refresh(db_bitacora)
    return db_bitacora

