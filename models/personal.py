import uuid
from datetime import datetime
from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey
from config.db import Base

class Personal(Base):
    __tablename__ = "tbb_personal"

    id = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    nombre = Column(String(100), nullable=False)
    apellido_paterno = Column(String(100), nullable=False)
    apellido_materno = Column(String(100), nullable=True)
    correo = Column(String(150), nullable=True)
    telefono = Column(String(20), nullable=True)

    puesto_id = Column(String(36), ForeignKey("tbd_puestos.id"), nullable=False)
    horario_id = Column(String(36), ForeignKey("tbd_horarios.horario_id"), nullable=False)
    especialidad_id = Column(String(36), ForeignKey("tbc_especialidades.id"), nullable=False)

    estatus = Column(Boolean, default=True)
    fecha_registro = Column(DateTime, default=datetime.utcnow)
    fecha_actualizacion = Column(DateTime, nullable=True, onupdate=datetime.utcnow)
