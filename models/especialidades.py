# models/especialidades.py

import uuid
from datetime import datetime
from sqlalchemy import Column, String, Boolean, DateTime
from config.db import Base

class Especialidad(Base):
    __tablename__ = "tbc_especialidades"

    id = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(255), nullable=True)
    estatus = Column(Boolean, default=True)
    fecha_registro = Column(DateTime, default=datetime.utcnow)
    fecha_actualizacion = Column(DateTime, nullable=True, onupdate=datetime.utcnow)
