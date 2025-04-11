# models/puestos.py

import uuid
from datetime import datetime
from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey
from config.db import Base

class Puesto(Base):
    __tablename__ = "tbd_puestos"

    id = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))  # UUID como string
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(255), nullable=True)
    departamento_id = Column(String(36), ForeignKey("tbc_departamentos.id"), nullable=False)  # UUID como string
    estatus = Column(Boolean, default=True)
    fecha_registro = Column(DateTime, default=datetime.utcnow)
    fecha_actualizacion = Column(DateTime, nullable=True, onupdate=datetime.utcnow)
    