# pylint: disable=too-few-public-methods
"""Esquemas Pydantic para Servicios Médicos y su asignación a Espacios."""

import datetime
from typing import Optional
from pydantic import BaseModel, Field, constr


class ServiciosMedicosEspaciosBase(BaseModel):
    """Esquema base para asignación de servicios médicos a espacios."""

    fk_servicio: str = Field(..., example="a111b222-c333-4d44-8888-eeeeffff0000")
    fk_espacio: str = Field(..., example="123e4567-e89b-12d3-a456-426614174000")
    observaciones: Optional[constr(max_length=255)] = Field(
        None, example="Este consultorio se usa solo en el turno matutino."
    )
    estatus_aprobacion: Optional[constr(max_length=20)] = Field(
        "Pendiente", example="Aprobado"
    )
    estatus: Optional[constr(max_length=20)] = Field(
        "Activo", example="Inactivo"
    )
    fecha_inicio: Optional[datetime.datetime] = Field(
        None, example="2025-04-01T08:00:00.000Z"
    )
    fecha_termino: Optional[datetime.datetime] = Field(
        None, example="2025-04-01T16:00:00.000Z"
    )


class ServiciosMedicosEspaciosCreate(ServiciosMedicosEspaciosBase):
    """Modelo para la creación de una asignación de servicio médico a un espacio."""


class ServiciosMedicosEspaciosUpdate(BaseModel):
    """Modelo para la actualización de una asignación de servicio médico a un espacio."""

    observaciones: Optional[constr(max_length=255)] = Field(
        None, example="Cambio de horario a la tarde."
    )
    estatus_aprobacion: Optional[constr(max_length=20)] = Field(
        None, example="Pendiente"
    )
    estatus: Optional[constr(max_length=20)] = Field(
        None, example="Activo"
    )
    fecha_inicio: Optional[datetime.datetime] = Field(
        None, example="2025-04-02T08:00:00.000Z"
    )
    fecha_termino: Optional[datetime.datetime] = Field(
        None, example="2025-04-02T16:00:00.000Z"
    )
    fecha_ultima_actualizacion: datetime.datetime = Field(
        default_factory=datetime.datetime.utcnow,
        example="2025-04-01T12:00:00.000Z"
    )


class ServiciosMedicosEspacios(ServiciosMedicosEspaciosBase):
    """Modelo de respuesta al consultar una asignación."""

    id: str = Field(..., example="9999cccc-dddd-4eee-aaaa-bbbbccccdddd")
    fecha_registro: Optional[datetime.datetime] = Field(
        None, example="2025-03-21T22:19:44.610Z"
    )
    fecha_ultima_actualizacion: Optional[datetime.datetime] = Field(
        None, example="2025-04-01T12:00:00.000Z"
    )

    class Config:
        from_attributes = True
