# schemas/horarios.py

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime, time
from uuid import UUID

class HorarioBase(BaseModel):
    nombre: str = Field(..., example="Turno Matutino")
    dia_semana: str = Field(..., example="Lunes")
    hora_inicio: time = Field(..., example="07:00")
    hora_fin: time = Field(..., example="15:00")
    turno: Optional[str] = Field(None, example="Matutino")
    estatus: Optional[bool] = Field(True, example=True)
    fecha_registro: Optional[datetime]
    fecha_actualizacion: Optional[datetime]

class HorarioCreate(HorarioBase):
    pass

class HorarioUpdate(BaseModel):
    nombre: Optional[str]
    dia_semana: Optional[str]
    hora_inicio: Optional[time]
    hora_fin: Optional[time]
    turno: Optional[str]
    estatus: Optional[bool]
    fecha_actualizacion: Optional[datetime]

class Horario(HorarioBase):
    id: UUID  # UUID como str

    class Config:
        orm_mode = True  # Asegura que Pydantic pueda convertir el objeto de SQLAlchemy a dict
