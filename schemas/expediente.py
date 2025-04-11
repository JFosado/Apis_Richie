"""Esquemas Pydantic para la entidad Expediente."""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from enum import Enum


class EstatusHabitosEnum(str, Enum):
    NINGUNO = "ninguno"
    OCASIONAL = "ocasional"
    FRECUENTE = "frecuente"


class EstatusActividadFisicaEnum(str, Enum):
    NULA = "nula"
    MODERADA = "moderada"
    INTENSA = "intensa"


class ExpedienteBase(BaseModel):
    """Campos base para un expediente."""
    id_paciente: int
    id_medico_responsable: int
    fecha_creacion: datetime
    antecedentes_personales: Optional[str] = None
    antecedentes_familiares: Optional[str] = None
    alergias: Optional[str] = None
    vacunas: Optional[str] = None
    habitos_tabaquismo: Optional[EstatusHabitosEnum] = EstatusHabitosEnum.NINGUNO
    habitos_alcohol: Optional[EstatusHabitosEnum] = EstatusHabitosEnum.NINGUNO
    habitos_drogas: Optional[EstatusHabitosEnum] = EstatusHabitosEnum.NINGUNO
    actividad_fisica: Optional[EstatusActividadFisicaEnum] = EstatusActividadFisicaEnum.MODERADA


class ExpedienteCreate(ExpedienteBase):
    """Esquema para la creación de un expediente."""
    fecha_creacion: datetime = datetime.utcnow()


class ExpedienteUpdate(BaseModel):
    """Esquema para la actualización de un expediente."""
    antecedentes_personales: Optional[str] = None
    antecedentes_familiares: Optional[str] = None
    alergias: Optional[str] = None
    vacunas: Optional[str] = None
    habitos_tabaquismo: Optional[EstatusHabitosEnum] = None
    habitos_alcohol: Optional[EstatusHabitosEnum] = None
    habitos_drogas: Optional[EstatusHabitosEnum] = None
    actividad_fisica: Optional[EstatusActividadFisicaEnum] = None


class ExpedienteResponse(ExpedienteBase):
    """Esquema de respuesta para un expediente."""
    id_expediente: int

    class Config:
        orm_mode = True