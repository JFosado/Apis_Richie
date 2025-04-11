from typing import List, Union
from pydantic import BaseModel, Field
from datetime import datetime

class RolBase(BaseModel):
    Nombre: str = Field(..., example="Administrador")  # Nombre del rol del sistema
    Descripcion: str = Field(..., example="Acceso completo a todos los módulos del sistema")  # Descripción del rol
    Estatus: bool = Field(..., example=True)  # Estado del rol: True = Activo, False = Inactivo
    Fecha_Registro: datetime = Field(..., example="2025-03-21T22:19:44.610Z")  # Fecha de creación
    Fecha_Actualizacion: datetime = Field(..., example="2025-04-01T10:00:00.000Z")  # Última modificación

class RolCreate(RolBase):
    """Modelo para la creación de un rol"""
    pass

class RolUpdate(RolBase):
    """Modelo para la actualización de un rol"""
    pass

class Rol(RolBase):
    """Modelo para la respuesta al consultar un rol"""
    ID: str = Field(..., example="f47ac10b-58cc-4372-a567-0e02b2c3d479")

    class Config:
        orm_mode = True
