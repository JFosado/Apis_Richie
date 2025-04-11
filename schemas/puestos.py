# schemas/puestos.py

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from uuid import UUID

class PuestoBase(BaseModel):
    nombre: str = Field(..., example="Jefe de Enfermería")
    descripcion: Optional[str] = Field(None, example="Responsable del personal de enfermería")
    departamento_id: UUID = Field(..., example="0c1d2e3f-4b9d-4a3e-9f61-48e8b7d4a5e3")  # UUID como str
    estatus: Optional[bool] = Field(True, example=True)
    fecha_registro: Optional[datetime] = Field(None, example="2025-04-01T10:00:00.000Z")
    fecha_actualizacion: Optional[datetime] = Field(None, example="2025-04-01T11:00:00.000Z")

class PuestoCreate(PuestoBase):
    pass

class PuestoUpdate(BaseModel):
    nombre: Optional[str]
    descripcion: Optional[str]
    departamento_id: Optional[UUID]  # UUID como str
    estatus: Optional[bool]
    fecha_actualizacion: Optional[datetime]

class Puesto(PuestoBase):
    id: UUID  # UUID como str

    class Config:
        orm_mode = True  # Asegura que Pydantic pueda convertir el objeto de SQLAlchemy a dict
