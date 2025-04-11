from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

class DepartamentoBase(BaseModel):
    nombre: str = Field(..., example="Departamento de Enfermería", description="Nombre del departamento")
    area_medica_id: Optional[str] = Field(
        None,
        example="f3e1b2d7-4b9d-4a3e-9f61-48e8b7d4a5e3",
        description="ID del área médica a la que pertenece el departamento"
    )
    departamento_superior_id: Optional[str] = Field(
        None,
        example="c1a2b3c4-d5e6-7f89-0123-456789abcdef",
        description="ID del departamento superior jerárquico (si aplica)"
    )
    responsable_id: Optional[str] = Field(
        None,
        example="123e4567-e89b-12d3-a456-426614174000",
        description="ID del responsable del departamento"
    )
    estatus: Optional[bool] = Field(
        True,
        example=True,
        description="Estado del departamento (activo/inactivo)"
    )
    fecha_registro: Optional[datetime] = Field(
        None,
        example="2025-03-25T08:00:00.000Z",
        description="Fecha en la que se registró el departamento (se genera automáticamente)"
    )
    fecha_actualizacion: Optional[datetime] = Field(
        None,
        example="2025-03-30T15:30:00.000Z",
        description="Última fecha de actualización del departamento"
    )

class DepartamentoCreate(DepartamentoBase):
    """Modelo para la creación de un departamento"""
    pass

class DepartamentoUpdate(BaseModel):
    """Modelo para la actualización parcial de un departamento"""
    nombre: Optional[str] = Field(None, example="Departamento de Urgencias", description="Nuevo nombre del departamento")
    area_medica_id: Optional[str] = Field(None, example="f3e1b2d7-4b9d-4a3e-9f61-48e8b7d4a5e3", description="Nuevo ID de área médica")
    departamento_superior_id: Optional[str] = Field(None, example="c1a2b3c4-d5e6-7f89-0123-456789abcdef", description="Nuevo ID de departamento superior")
    responsable_id: Optional[str] = Field(None, example="123e4567-e89b-12d3-a456-426614174000", description="Nuevo responsable del departamento")
    estatus: Optional[bool] = Field(None, example=False, description="Nuevo estado del departamento")
    fecha_actualizacion: Optional[datetime] = Field(None, example="2025-04-01T12:00:00.000Z", description="Fecha de actualización (se puede enviar o generar automáticamente)")

class Departamento(DepartamentoBase):
    """Modelo para la respuesta al consultar un departamento"""
    id: str = Field(..., example="0c1d2e3f-4a5b-6789-0abc-def123456789", description="Identificador único del departamento")

    class Config:
        orm_mode = True
