from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Optional

# 🔹 Esquema base para los servicios médicos
class ServiceMBase(BaseModel):
    nombre: str = Field(..., example="Consulta General")
    descripcion: Optional[str] = Field(None, example="Atención médica general para diagnóstico y evaluación.")
    observaciones: Optional[str] = Field(None, example="Este servicio se brinda de lunes a viernes de 8 AM a 5 PM.")
    fecha_registro: Optional[datetime] = Field(None, example="2025-03-21T22:19:44.610Z")
    fecha_actualizacion: Optional[datetime] = Field(None, example="2025-03-21T22:19:44.610Z")

# 🔹 Modelo para la creación de un servicio médico
class ServiceMCreate(ServiceMBase):
    pass

# 🔹 Modelo para la actualización de un servicio médico
class ServiceMUpdate(BaseModel):
    nombre: Optional[str] = Field(None, example="Consulta Pediátrica")
    descripcion: Optional[str] = Field(None, example="Consulta médica especializada en niños y adolescentes.")
    observaciones: Optional[str] = Field(None, example="Disponible solo en el turno matutino.")
    fecha_actualizacion: Optional[datetime] = Field(None, example="2025-03-22T10:00:00.000Z")

# 🔹 Modelo para la respuesta al consultar un servicio médico
class Service(ServiceMBase):
    id: str = Field(..., example="b3c7e9b2-8429-4c71-ae68-61c30269c237")
    model_config = ConfigDict(from_attributes=True)
