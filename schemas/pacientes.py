"""Esquemas Pydantic para la entidad Paciente."""

from datetime import datetime
from typing import Optional
from enum import Enum
from pydantic import BaseModel


class EstatusVidaEnum(str, Enum):
    """Enumeración del estatus de vida del paciente."""
    VIVO = "Vivo"
    FINADO = "Finado"
    COMA = "Coma"
    VEGETATIVO = "Vegetativo"


class PacienteBase(BaseModel):
    """Campos base para un paciente."""
    Persona_ID: int
    NSS: int
    Tipo_de_seguro: Optional[str] = None
    Fecha_ultima_cita: Optional[datetime] = None
    Estatus_Medico: Optional[str] = None
    Estatus_vida: Optional[EstatusVidaEnum] = None
    Estatus: Optional[bool] = True


class PacienteCreate(PacienteBase):
    """Esquema para la creación de un paciente."""


class PacienteUpdate(BaseModel):
    """Esquema para la actualización de un paciente."""
    Persona_ID: Optional[int] = None
    NSS: Optional[int] = None
    Tipo_de_seguro: Optional[str] = None
    Fecha_ultima_cita: Optional[datetime] = None
    Estatus_Medico: Optional[str] = None
    Estatus_vida: Optional[EstatusVidaEnum] = None
    Estatus: Optional[bool] = None
    Fecha_Actualizacion: Optional[datetime] = None


class PacienteResponse(PacienteBase):
    """Esquema de respuesta para un paciente."""
    ID: int
    Fecha_Registro: Optional[datetime] = None
    Fecha_Actualizacion: Optional[datetime] = None

    class Config:
        orm_mode = True
