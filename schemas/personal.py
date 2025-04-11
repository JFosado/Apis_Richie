from typing import Optional
from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from uuid import UUID

class PersonalBase(BaseModel):
    nombre: str = Field(..., example="Luis")
    apellido_paterno: str = Field(..., example="González")
    apellido_materno: Optional[str] = Field(None, example="Ramírez")
    correo: Optional[EmailStr] = Field(None, example="luis@example.com")
    telefono: Optional[str] = Field(None, example="2223456789")

    puesto_id: UUID = Field(..., example="uuid-del-puesto")
    horario_id: UUID = Field(..., example="uuid-del-horario")
    especialidad_id: UUID = Field(..., example="uuid-especialidad")

    estatus: Optional[bool] = Field(True, example=True)
    fecha_registro: Optional[datetime]
    fecha_actualizacion: Optional[datetime]

class PersonalCreate(PersonalBase):
    pass

class PersonalUpdate(BaseModel):
    nombre: Optional[str]
    apellido_paterno: Optional[str]
    apellido_materno: Optional[str]
    correo: Optional[EmailStr]
    telefono: Optional[str]
    puesto_id: Optional[UUID]
    horario_id: Optional[UUID]
    especialidad_id: Optional[UUID]
    estatus: Optional[bool]
    fecha_actualizacion: Optional[datetime]

class Personal(PersonalBase):
    id: UUID

    class Config:
        orm_mode = True
