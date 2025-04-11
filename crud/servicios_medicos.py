import models.servicios_medicos
import schemas.servicios_medicos
from sqlalchemy.orm import Session

# 🔹 Obtener un servicio médico por ID
def get_serviceM(db: Session, id: str):
    """
    Retorna un servicio médico por su ID.
    """
    return db.query(models.servicios_medicos.ServiceM).filter(
        models.servicios_medicos.ServiceM.id == id
    ).first()

# 🔹 Obtener un servicio médico por su nombre exacto
def get_serviceM_by_nombre(db: Session, nombre: str):
    """
    Retorna el servicio médico que coincida exactamente con el nombre proporcionado.
    """
    return db.query(models.servicios_medicos.ServiceM).filter(
        models.servicios_medicos.ServiceM.nombre == nombre
    ).first()

# 🔹 Obtener todos los servicios médicos registrados (con paginación)
def get_servicesM(db: Session, skip: int = 0, limit: int = 10):
    """
    Retorna una lista de servicios médicos con paginación.
    """
    return db.query(models.servicios_medicos.ServiceM).offset(skip).limit(limit).all()

# 🔹 Crear un nuevo servicio médico
def create_serviceM(db: Session, service: schemas.servicios_medicos.ServiceMCreate):
    """
    Crea y guarda un nuevo servicio médico en la base de datos.
    """
    db_serviceM = models.servicios_medicos.ServiceM(
        nombre=service.nombre,
        descripcion=service.descripcion,
        observaciones=service.observaciones,
        fecha_registro=service.fecha_registro,
        fecha_actualizacion=service.fecha_actualizacion
    )
    db.add(db_serviceM)
    db.commit()
    db.refresh(db_serviceM)
    return db_serviceM

# 🔹 Actualizar los datos de un servicio médico por ID
def update_serviceM(db: Session, id: str, service: schemas.servicios_medicos.ServiceMUpdate):
    """
    Actualiza solo los campos proporcionados de un servicio médico existente.
    """
    db_serviceM = db.query(models.servicios_medicos.ServiceM).filter(
        models.servicios_medicos.ServiceM.id == id
    ).first()
    if db_serviceM:
        for key, value in service.model_dump(exclude_unset=True).items():
            setattr(db_serviceM, key, value)
        db.commit()
        db.refresh(db_serviceM)
    return db_serviceM

# 🔹 Eliminar un servicio médico por ID
def delete_serviceM(db: Session, id: str):
    """
    Elimina un servicio médico de la base de datos si existe.
    """
    db_serviceM = db.query(models.servicios_medicos.ServiceM).filter(
        models.servicios_medicos.ServiceM.id == id
    ).first()
    if db_serviceM:
        db.delete(db_serviceM)
        db.commit()
    return db_serviceM
