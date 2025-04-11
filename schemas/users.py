from typing import Optional
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    persona_id: UUID = Field(..., alias="Persona_ID", example="2d2f0e84-19d0-4fa4-81e3-8ddcbd2b94e0")
    nombre_usuario: str = Field(..., alias="Nombre_Usuario", example="juanperez")
    correo_electronico: EmailStr = Field(..., alias="Correo_Electronico", example="juan.perez@example.com")
    contrasena: str = Field(..., alias="Contrasena", example="MiContrasenaSegura123")
    numero_telefonico_movil: Optional[str] = Field(None, alias="Numero_Telefonico_Movil", example="5551234567")
    estatus: str = Field(default="Activo", alias="Estatus", example="Activo")

    class Config:
        allow_population_by_field_name = True
        from_attributes = True


class UserCreate(UserBase):
    """Modelo para crear un usuario."""


class UserUpdate(BaseModel):
    persona_id: Optional[UUID] = Field(None, alias="Persona_ID")
    nombre_usuario: Optional[str] = Field(None, alias="Nombre_Usuario")
    correo_electronico: Optional[EmailStr] = Field(None, alias="Correo_Electronico")
    contrasena: Optional[str] = Field(None, alias="Contrasena")
    numero_telefonico_movil: Optional[str] = Field(None, alias="Numero_Telefonico_Movil")
    estatus: Optional[str] = Field(None, alias="Estatus")
    fecha_actualizacion: Optional[datetime] = Field(None, alias="Fecha_Actualizacion")

    class Config:
        allow_population_by_field_name = True
        from_attributes = True


class User(UserBase):
    id: UUID = Field(..., alias="ID", example="1a2b3c4d-5e6f-7890-abcd-1234567890ef")
    fecha_registro: Optional[datetime] = Field(None, alias="Fecha_Registro", example="2025-03-21T22:19:44.610Z")
    fecha_actualizacion: Optional[datetime] = Field(None, alias="Fecha_Actualizacion", example="2025-03-21T22:19:44.610Z")

    class Config:
        allow_population_by_field_name = True
        from_attributes = True


class UserLogin(BaseModel):
    nombre_usuario: Optional[str] = Field(None, alias="Nombre_Usuario", example="juanperez")
    correo_electronico: Optional[EmailStr] = Field(None, alias="Correo_Electronico", example="juan.perez@example.com")
    contrasena: str = Field(..., alias="Contrasena", example="MiContrasenaSegura123")
    numero_telefonico_movil: Optional[str] = Field(None, alias="Numero_Telefonico_Movil", example="5551234567")

    class Config:
        allow_population_by_field_name = True
