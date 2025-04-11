from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class UserBase(BaseModel):
    Persona_ID: str = Field(..., example="2d2f0e84-19d0-4fa4-81e3-8ddcbd2b94e0")
    Nombre_Usuario: str = Field(..., example="juanperez")  # Nombre único de usuario
    Correo_Electronico: EmailStr = Field(..., example="juan.perez@example.com")  # Correo válido
    Contrasena: str = Field(..., example="MiContrasenaSegura123")  # Contraseña en texto plano (se cifra antes de guardar)
    Numero_Telefonico_Movil: Optional[str] = Field(None, example="5551234567")  # Teléfono móvil opcional
    Estatus: str = Field(default="Activo", example="Activo")  # Estado del usuario (Activo/Inactivo)
    Fecha_Registro: Optional[datetime] = Field(None, example="2025-03-21T22:19:44.610Z")  # Fecha de creación
    Fecha_Actualizacion: Optional[datetime] = Field(None, example="2025-03-21T22:19:44.610Z")  # Fecha de última actualización

class UserCreate(UserBase):
    """Modelo para la creación de un usuario"""
    pass

class UserUpdate(UserBase):
    """Modelo para la actualización de un usuario"""
    pass

class User(UserBase):
    """Modelo para la respuesta al consultar un usuario"""
    ID: str = Field(..., example="1a2b3c4d-5e6f-7890-abcd-1234567890ef")

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    """Modelo para iniciar sesión con cualquier dato único"""
    Nombre_Usuario: Optional[str] = Field(None, example="juanperez")
    Correo_Electronico: Optional[EmailStr] = Field(None, example="juan.perez@example.com")
    Contrasena: str = Field(..., example="MiContrasenaSegura123")
    Numero_Telefonico_Movil: Optional[str] = Field(None, example="5551234567")
