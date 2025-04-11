from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime, date
from uuid import UUID

# 🔹 Base común
class PersonBase(BaseModel):
    Titulo_Cortesia: Optional[str] = Field(None, example="Dr.")
    Nombre: str = Field(..., example="Carlos")
    Primer_Apellido: str = Field(..., example="Ramírez")
    Segundo_Apellido: Optional[str] = Field(None, example="Gómez")
    CURP: str = Field(..., example="RAGC890101HDFLNN09")
    Correo_Electronico: str = Field(..., example="carlos.ramirez@example.com")
    Telefono: Optional[str] = Field(None, example="5551234567")
    Fecha_Nacimiento: date = Field(..., example="1989-01-01")
    Fotografia: Optional[str] = Field(None, example="https://example.com/photo.jpg")
    Genero: str = Field(..., example="Masculino")
    Tipo_Sangre: str = Field(..., example="O+")
    Estatus: bool = Field(..., example=True)
    Fecha_Registro: Optional[datetime] = Field(None, example="2025-03-21T22:19:44.610Z")
    Fecha_Actualizacion: Optional[datetime] = Field(None, example="2025-03-21T22:19:44.610Z")

# 🔹 Crear persona
class PersonCreate(PersonBase):
    """Modelo para la creación de una persona"""
    pass

# 🔹 Actualizar persona (parcial)
class PersonUpdate(BaseModel):
    """Modelo para la actualización de una persona (parcial)"""

    Titulo_Cortesia: Optional[str] = Field(None, example="Dr.")
    Nombre: Optional[str] = Field(None, example="Carlos")
    Primer_Apellido: Optional[str] = Field(None, example="Ramírez")
    Segundo_Apellido: Optional[str] = Field(None, example="Gómez")
    CURP: Optional[str] = Field(None, example="RAGC890101HDFLNN09")
    Correo_Electronico: Optional[str] = Field(None, example="carlos.ramirez@example.com")
    Telefono: Optional[str] = Field(None, example="5551234567")
    Fecha_Nacimiento: Optional[date] = Field(None, example="1989-01-01")
    Fotografia: Optional[str] = Field(None, example="https://example.com/photo.jpg")
    Genero: Optional[str] = Field(None, example="Masculino")
    Tipo_Sangre: Optional[str] = Field(None, example="O+")
    Estatus: Optional[bool] = Field(None, example=True)
    Fecha_Actualizacion: Optional[datetime] = Field(None, example="2025-03-21T22:19:44.610Z")

# 🔹 Modelo de respuesta
class Person(PersonBase):
    """Modelo para la respuesta al consultar una persona"""
    ID: UUID = Field(..., example="3fa85f64-5717-4562-b3fc-2c963f66afa6")

    class Config:
        from_attributes = True
