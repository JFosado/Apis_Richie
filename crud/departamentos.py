from sqlalchemy.orm import Session
import models.departamentos as models
import schemas.departamentos as schemas
from datetime import datetime

# 🔹 Obtener un departamento por ID
def get_departamento(db: Session, departamento_id: str):
    return db.query(models.Departamentos).filter(models.Departamentos.id == departamento_id).first()

# 🔹 Obtener todos los departamentos con paginación
def get_departamentos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Departamentos).offset(skip).limit(limit).all()

# 🔹 Crear un nuevo departamento
def create_departamento(db: Session, departamento: schemas.DepartamentoCreate):
    db_departamento = models.Departamentos(
        nombre=departamento.nombre,
        area_medica_id=departamento.area_medica_id,
        departamento_superior_id=departamento.departamento_superior_id,
        responsable_id=departamento.responsable_id,
        estatus=departamento.estatus,
        fecha_registro=datetime.utcnow()
    )
    db.add(db_departamento)
    try:
        db.commit()
        db.refresh(db_departamento)
    except Exception as e:
        db.rollback()
        raise e
    return db_departamento

# 🔹 Actualizar un departamento por ID
def update_departamento(db: Session, departamento_id: str, departamento_data: schemas.DepartamentoUpdate):
    db_departamento = db.query(models.Departamentos).filter(models.Departamentos.id == departamento_id).first()
    if db_departamento:
        for var, value in departamento_data.dict(exclude_unset=True).items():
            if value is not None:
                setattr(db_departamento, var, value)
        db_departamento.fecha_actualizacion = datetime.utcnow()
        try:
            db.commit()
            db.refresh(db_departamento)
        except Exception as e:
            db.rollback()
            raise e
    return db_departamento

# 🔹 Eliminar un departamento por ID
def delete_departamento(db: Session, departamento_id: str):
    db_departamento = db.query(models.Departamentos).filter(models.Departamentos.id == departamento_id).first()
    if db_departamento:
        try:
            db.delete(db_departamento)
            db.commit()
        except Exception as e:
            db.rollback()
            raise e
    return db_departamento
