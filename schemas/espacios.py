# pylint: disable=too-few-public-methods
"""Esquemas Pydantic para el modelo de Espacios hospitalarios."""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, constr, Field

class EspacioBase(BaseModel):
    """Base común para los esquemas de espacio."""

    tipo: constr(max_length=50) = Field(..., example="Consultorio")
    nombre: constr(max_length=100) = Field(..., example="Consultorio 101")
    departamento_id: Optional[str] = Field(
        None, example="deba1099-c9e4-44f6-b03e-193f871d71df"
    )
    estatus: constr(max_length=20) = Field(..., example="Activo")
    capacidad: Optional[int] = Field(None, example=5)
    espacio_superior_id: Optional[str] = Field(
        None, example="47fa1262-0c87-4a2a-b037-17dbf719d723"
    )

class EspacioCreate(EspacioBase):
    """Modelo para la creación de un espacio hospitalario."""

class EspacioUpdate(BaseModel):
    """Modelo para la actualización de un espacio hospitalario."""

    tipo: Optional[constr(max_length=50)] = Field(None, example="Sala de Operaciones")
    nombre: Optional[constr(max_length=100)] = Field(None, example="Quirófano Principal")
    departamento_id: Optional[str] = Field(
        None, example="deba1099-c9e4-44f6-b03e-193f871d71df"
    )
    estatus: Optional[constr(max_length=20)] = Field(None, example="Inactivo")
    capacidad: Optional[int] = Field(None, example=10)
    espacio_superior_id: Optional[str] = Field(
        None, example="47fa1262-0c87-4a2a-b037-17dbf719d723"
    )
    fecha_actualizacion: datetime = Field(
        default_factory=datetime.utcnow,
        example="2025-04-02T12:00:00.000Z"
    )

class Espacio(EspacioBase):
    """Modelo para la respuesta al consultar un espacio hospitalario."""

    id: str = Field(..., example="81c4a9a2-8b22-49e9-b2ed-713071de0f8e")
    fecha_registro: Optional[datetime] = Field(
        None, example="2025-03-21T22:19:44.610Z"
    )
    fecha_actualizacion: Optional[datetime] = Field(
        None, example="2025-04-01T12:00:00.000Z"
    )

    class Config:
        """Activa el modo ORM para compatibilidad con SQLAlchemy."""
        from_attributes = True
