from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal
from models.personal_medico import EnumTipoPersonal, EnumEstatus


class PersonalMedicoBase(BaseModel):
    """Campos base para un registro de personal médico."""
    Persona_ID: int
    Departamento_ID: int
    Cedula_Profesional: str
    Tipo: EnumTipoPersonal
    Especialidad: str
    Fecha_Contratacion: datetime
    Fecha_Termino_Contrato: datetime
    Salario: Decimal
    Estatus: EnumEstatus


class PersonalMedicoCreate(PersonalMedicoBase):
    """Esquema para la creación de un registro de personal médico."""


class PersonalMedicoUpdate(BaseModel):
    """Esquema para la actualización parcial de un registro de personal médico."""
    Departamento_ID: Optional[int] = None
    Cedula_Profesional: Optional[str] = None
    Tipo: Optional[EnumTipoPersonal]
