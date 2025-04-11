import models.solicitudes
import schemas.solicitudes
from sqlalchemy.orm import Session

def get_request(db: Session, id: int):
    return db.query(models.solicitudes.Solicitud).filter(models.solicitudes.Solicitud.ID == id).first()

def get_requests(db: Session, skip: int = 0, limit: int = 50):
    return db.query(models.solicitudes.Solicitud).offset(skip).limit(limit).all()

def create_request(db: Session, req: schemas.solicitudes.SolicitudCreate):
    db_request = models.solicitudes.Solicitud(
        Paciente_ID=req.Paciente_ID, 
        Medico_ID=req.Medico_ID, 
        Servicio_ID=req.Servicio_ID,
        Prioridad=req.Prioridad, 
        Descripcion=req.Descripcion, 
        Estatus=req.Estatus, 
        Estatus_Aprobacion=req.Estatus_Aprobacion,
        Fecha_Registro=req.Fecha_Registro, 
        Fecha_Actualizacion=req.Fecha_Actualizacion
    )
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request

def update_request(db: Session, id: int, req: schemas.solicitudes.SolicitudUpdate):
    db_request = db.query(models.solicitudes.Solicitud).filter(models.solicitudes.Solicitud.ID == id).first()
    if db_request:
        for var, value in vars(req).items():
            setattr(db_request, var, value) if value else None
        db.commit()
        db.refresh(db_request)
    return db_request

def delete_request(db: Session, id: int):
    db_request = db.query(models.solicitudes.Solicitud).filter(models.solicitudes.Solicitud.ID == id).first()
    if db_request:
        db.delete(db_request)
        db.commit()
    return db_request