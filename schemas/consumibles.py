# pylint: disable=too-few-public-methods
"""Esquemas Pydantic para el modelo de Consumibles médicos."""

from datetime import datetime
from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field, constr

class ConsumibleBase(BaseModel):
    """Base para los esquemas de consumibles médicos."""

    nombre: str = Field(..., example="Guantes de látex")
    descripcion: str = Field(..., example="Guantes estériles de un solo uso, talla mediana")
    tipo: constr(max_length=50) = Field(..., example="Insumo")  # Coincide con el Enum
    departamento_id: Optional[UUID] = Field(
        None, example="2fc0d5d1-62b4-4a32-a9b7-9deac7f78d19"
    )
    cantidad_existencia: int = Field(..., example=150)
    detalle: Optional[str] = Field(None, example="Caja con 100 unidades")
    estatus: Optional[bool] = Field(None, example=True)
    observaciones: Optional[str] = Field(None, example="Usar antes del 2025-12-01")
    espacio_medico: Optional[str] = Field(None, example="Almacén Central")
    fecha_registro: Optional[datetime] = Field(
        None,
        example="2025-03-21T22:19:44.610Z"
    )
    fecha_actualizacion: Optional[datetime] = Field(
        None,
        example="2025-04-01T10:00:00.000Z"
    )


class ConsumibleCreate(ConsumibleBase):
    """Modelo para la creación de un consumible médico."""


class ConsumibleUpdate(BaseModel):
    """Modelo para la actualización parcial de un consumible médico."""

    nombre: Optional[str] = Field(None, example="Guantes de nitrilo")
    descripcion: Optional[str] = Field(None, example="Guantes hipoalergénicos, talla grande")
    tipo: Optional[constr(max_length=50)] = Field(None, example="Equipo")
    departamento_id: Optional[UUID] = Field(None, example="2fc0d5d1-62b4-4a32-a9b7-9deac7f78d19")
    cantidad_existencia: Optional[int] = Field(None, example=200)
    detalle: Optional[str] = Field(None, example="Caja con 50 pares")
    estatus: Optional[bool] = Field(None, example=False)
    observaciones: Optional[str] = Field(None, example="Cambio de proveedor")
    espacio_medico: Optional[str] = Field(None, example="Almacén 2")
    fecha_actualizacion: Optional[datetime] = Field(
        None,
        example="2025-04-05T09:30:00.000Z"
    )


class Consumible(ConsumibleBase):
    """Modelo para la respuesta al consultar un consumible médico."""

    id: UUID = Field(..., example="3e79d145-397a-4e50-bb74-8c6a88c93fa2")

    class Config:
        from_attributes = True
