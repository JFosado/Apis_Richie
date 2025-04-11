from typing import Optional
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, Field


class UserRolBase(BaseModel):
    usuario_id: UUID = Field(..., alias="Usuario_ID", example="b5cb2487-e6ac-4419-9916-47a10d4f4103")
    rol_id: UUID = Field(..., alias="Rol_ID", example="d7c2e7f8-5ac4-4d0b-8e3b-fbe2216c4a2c")
    estatus: bool = Field(..., alias="Estatus", example=True)

    class Config:
        allow_population_by_field_name = True
        from_attributes = True


class UserRolCreate(UserRolBase):
    """Modelo para crear una asignación de usuario a rol."""


class UserRolUpdate(BaseModel):
    estatus: Optional[bool] = Field(None, alias="Estatus", example=True)
    fecha_actualizacion: Optional[datetime] = Field(None, alias="Fecha_Actualizacion", example="2025-03-28T09:15:00")

    class Config:
        allow_population_by_field_name = True
        from_attributes = True


class UserRol(UserRolBase):
    fecha_registro: Optional[datetime] = Field(None, alias="Fecha_Registro", example="2025-03-21T14:30:00")
    fecha_actualizacion: Optional[datetime] = Field(None, alias="Fecha_Actualizacion", example="2025-03-28T09:15:00")

    class Config:
        allow_population_by_field_name = True
        from_attributes = True
