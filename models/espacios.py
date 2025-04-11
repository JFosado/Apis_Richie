# pylint: disable=too-few-public-methods, invalid-name, non-ascii-name
"""Modelo ORM para representar los espacios físicos del hospital."""

import enum
import uuid
import datetime
from sqlalchemy import Column, String, Enum, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
from config.db import Base

class TipoEspacioEnum(str, enum.Enum):
    """
    Enumeración de tipos de espacios disponibles en el hospital.
    """
    Consultorio = 'Consultorio'
    Laboratorio = 'Laboratorio'
    Quirófano = 'Quirófano'
    Sala_de_Espera = 'Sala de Espera'
    Edificio = 'Edificio'
    Estacionamiento = 'Estacionamiento'
    Habitación = 'Habitación'
    Cama = 'Cama'
    Sala_Maternidad = 'Sala Maternidad'
    Cunero = 'Cunero'
    Anfiteatro = 'Anfiteatro'
    Oficina = 'Oficina'
    Sala_de_Juntas = 'Sala de Juntas'
    Auditorio = 'Auditorio'
    Cafeteria = 'Cafeteria'
    Capilla = 'Capilla'
    Farmacia = 'Farmacia'
    Ventanilla = 'Ventanilla'
    Recepción = 'Recepción'
    Piso = 'Piso'


class EstatusEnum(str, enum.Enum):
    """
    Enumeración para el estatus del espacio.
    """
    Activo = 'Activo'
    Inactivo = 'Inactivo'


class Espacio(Base):
    """
    Modelo que representa un espacio físico dentro del hospital.
    """
    __tablename__ = 'tbc_espacios'

    id = Column(
        String(36),
        primary_key=True,
        index=True,
        default=lambda: str(uuid.uuid4())
    )
    tipo = Column(Enum(TipoEspacioEnum), nullable=False)
    nombre = Column(String(100), nullable=False)

    departamento_id = Column(
        String(36),
        ForeignKey("tbc_departamentos.id", ondelete="SET NULL"),
        nullable=True,
        index=True
    )
    estatus = Column(
        Enum(EstatusEnum),
        nullable=False,
        default=EstatusEnum.Activo
    )
    fecha_registro = Column(
        DateTime,
        default=datetime.datetime.utcnow
    )
    fecha_actualizacion = Column(
        DateTime,
        nullable=True,
        onupdate=datetime.datetime.utcnow
    )
    capacidad = Column(Integer, nullable=True)

    espacio_superior_id = Column(
        String(36),
        ForeignKey("tbc_espacios.id", ondelete="SET NULL"),
        nullable=True
    )

    servicios_medicos_espacios = relationship(
        "ServiciosMedicosEspacios",
        back_populates="espacio"
    )

    citas = relationship("CitaMedica", back_populates="espacio")
