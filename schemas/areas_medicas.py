# pylint: disable=too-few-public-methods
"""Esquemas Pydantic para el modelo de Área Médica."""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class AreaMedicaBase(BaseModel):
    """Base para los esquemas de área médica."""

    Nombre: str = Field(..., example="Cardiología", description="Nombre del área médica")
    Descripcion: Optional[str] = Field(
        None,
        example="Área especializada en el tratamiento del corazón",
        description="Descripción breve del área"
    )
    Estatus: Optional[bool] = Field(
        True,
        example=True,
        description="Indica si el área médica está activa"
    )
    Fecha_Registro: Optional[datetime] = Field(
        None,
        example="2025-03-21T22:19:44.610Z",
        description=(
            "Fecha en la que se registró el área médica "
            "(opcional, se genera automáticamente)"
        )
    )
    Fecha_Actualizacion: Optional[datetime] = Field(
        None,
        example="2025-04-01T10:00:00.000Z",
        description="Última fecha de actualización (opcional, se genera automáticamente)"
    )


class AreaMedicaCreate(AreaMedicaBase):
    """Modelo para la creación de un área médica."""


class AreaMedicaUpdate(BaseModel):
    """Modelo para la actualización parcial de un área médica."""

    Nombre: Optional[str] = Field(
        None,
        example="Neurología",
        description="Nuevo nombre del área médica"
    )
    Descripcion: Optional[str] = Field(
        None,
        example="Área que trata enfermedades del sistema nervioso",
        description="Nueva descripción"
    )
    Estatus: Optional[bool] = Field(
        None,
        example=False,
        description="Nuevo estatus del área médica"
    )
    Fecha_Actualizacion: Optional[datetime] = Field(
        None,
        example="2025-04-05T09:30:00.000Z",
        description="Fecha de actualización (opcional, se genera automáticamente si no se envía)"
    )


class AreaMedica(AreaMedicaBase):
    """Modelo para la respuesta al consultar un área médica."""

    ID: str = Field(
        ...,
        example="9b4e1bc0-8129-4cf5-9e7c-1c802e60decd",
        description="Identificador único del área médica"
    )

    class Config:
        """Configuración para activar el modo ORM."""
        orm_mode = True
