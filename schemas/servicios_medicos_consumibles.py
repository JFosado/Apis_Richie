# pylint: disable=too-few-public-methods
"""Esquemas Pydantic para Servicios Médicos Consumibles."""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict


class ServiciosMedicosConsumiblesBase(BaseModel):
    """Esquema base para consumibles usados en servicios médicos."""

    id_servicio: str
    id_consumible: str
    cantidad_usada: int
    fecha_uso: Optional[datetime] = None
    observaciones: Optional[str] = None


class ServiciosMedicosConsumiblesCreate(ServiciosMedicosConsumiblesBase):
    """Modelo para la creación de un registro de servicio médico y consumible."""


class ServiciosMedicosConsumiblesUpdate(BaseModel):
    """Modelo para la actualización parcial de un registro de consumible usado."""

    cantidad_usada: Optional[int] = None
    fecha_uso: Optional[datetime] = None
    observaciones: Optional[str] = None


class ServiciosMedicosConsumibles(ServiciosMedicosConsumiblesBase):
    """Modelo de respuesta con ID incluido."""

    id: str

    model_config = ConfigDict(from_attributes=True)
