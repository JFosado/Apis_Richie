# pylint: disable=too-few-public-methods
"""Modelo ORM para representar consumibles usados en un servicio médico específico."""

import uuid
from sqlalchemy import Column, String, ForeignKey, DateTime, Text, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from config.db import Base

class ServiciosMedicosConsumibles(Base):
    """
    Representa los consumibles utilizados en un servicio médico específico.
    """

    __tablename__ = "tbd_servicios_medicos_consumibles"

    id = Column(
        String(36),
        primary_key=True,
        index=True,
        default=lambda: str(uuid.uuid4())
    )
    id_servicio = Column(
        String(36),
        ForeignKey("tbc_servicios_medicos.id", ondelete="CASCADE"),
        nullable=False
    )
    id_consumible = Column(
        String(36),
        ForeignKey("tbc_consumibles.id", ondelete="CASCADE"),
        nullable=False
    )
    cantidad_usada = Column(Integer, nullable=False)
    fecha_uso = Column(
        DateTime,
        nullable=False,
        server_default=func.now()
    )
    observaciones = Column(Text, nullable=True)

    servicio = relationship("ServiceM", back_populates="consumibles")
    consumible = relationship("Consumible", back_populates="servicios")
