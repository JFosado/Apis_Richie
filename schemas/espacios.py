from datetime import datetime
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field

class EspacioBase(BaseModel):
    tipo: str = Field(..., max_length=50, example="Consultorio")
    nombre: str = Field(..., max_length=100, example="Consultorio 101")
    departamento_id: Optional[UUID] = Field(
        None, example="deba1099-c9e4-44f6-b03e-193f871d71df"
    )
    estatus: str = Field(..., max_length=20, example="Activo")
    capacidad: Optional[int] = Field(None, example=5)
    espacio_superior_id: Optional[UUID] = Field(
        None, example="47fa1262-0c87-4a2a-b037-17dbf719d723"
    )

class EspacioCreate(EspacioBase):
    """Modelo para la creación de un espacio hospitalario."""

class EspacioUpdate(BaseModel):
    tipo: Optional[str] = Field(None, max_length=50, example="Sala de Operaciones")
    nombre: Optional[str] = Field(None, max_length=100, example="Quirófano Principal")
    departamento_id: Optional[UUID] = Field(
        None, example="deba1099-c9e4-44f6-b03e-193f871d71df"
    )
    estatus: Optional[str] = Field(None, max_length=20, example="Inactivo")
    capacidad: Optional[int] = Field(None, example=10)
    espacio_superior_id: Optional[UUID] = Field(
        None, example="47fa1262-0c87-4a2a-b037-17dbf719d723"
    )
    fecha_actualizacion: Optional[datetime] = Field(
        None, example="2025-04-02T12:00:00.000Z"
    )

class EspacioResponse(EspacioBase):
    id: UUID
    fecha_registro: Optional[datetime] = Field(
        None, example="2025-03-21T22:19:44.610Z"
    )
    fecha_actualizacion: Optional[datetime] = Field(
        None, example="2025-04-01T12:00:00.000Z"
    )

    class Config:
        from_attributes = True
