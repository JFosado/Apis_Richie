# schemas/especialidades.py

from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID

class EspecialidadBase(BaseModel):
    nombre: str = Field(..., example="Cardiología")
    descripcion: Optional[str] = Field(None, example="Especialidad enfocada en el corazón")
    estatus: Optional[bool] = Field(True, example=True)
    fecha_registro: Optional[datetime]
    fecha_actualizacion: Optional[datetime]

class EspecialidadCreate(EspecialidadBase):
    pass

class EspecialidadUpdate(BaseModel):
    nombre: Optional[str]
    descripcion: Optional[str]
    estatus: Optional[bool]
    fecha_actualizacion: Optional[datetime]

class Especialidad(EspecialidadBase):
    id: UUID

    class Config:
        orm_mode = True
