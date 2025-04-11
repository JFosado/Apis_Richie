# pylint: disable=too-few-public-methods
"""Modelo ORM para representar las áreas médicas del hospital."""

from datetime import datetime
import uuid
from sqlalchemy import Column, String, Text, DateTime, Boolean, text
from sqlalchemy.orm import relationship
from config.db import Base

class AreaMedica(Base):
    """
    Representa un área médica dentro del hospital
    (por ejemplo: Pediatría, Cardiología, Urgencias).
    """

    __tablename__ = "tbc_areas_medicas"

    ID = Column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        nullable=False
    )
    Nombre = Column(String(150), nullable=False)
    Descripcion = Column(Text, nullable=True)
    Estatus = Column(Boolean, default=True, nullable=False)
    Fecha_Registro = Column(
        DateTime,
        nullable=False,
        server_default=text('CURRENT_TIMESTAMP')
    )
    Fecha_Actualizacion = Column(
        DateTime,
        nullable=True,
        onupdate=datetime.utcnow
    )
    
    departamentos = relationship("Departamentos", back_populates="area_medica")

    def __repr__(self):
        return (
            f"<AreaMedica(ID={self.ID}, Nombre='{self.Nombre}', "
            f"Estatus='{self.Estatus}')>"
        )
