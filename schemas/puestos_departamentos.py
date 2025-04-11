from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class TurnoEnum(str, Enum):
    Mañana = "Mañana"
    Tarde = "Tarde"
    Noche = "Noche"

class PuestoDepartamentoBase(BaseModel):
    Nombre: str
    Descripcion: Optional[str] = None
    Salario: Optional[float] = None
    Turno: Optional[TurnoEnum] = None
    DepartamentoID: int

class PuestoDepartamentoCreate(PuestoDepartamentoBase):
    Creado: Optional[datetime] = None
    Modificado: Optional[datetime] = None

class PuestoDepartamentoUpdate(PuestoDepartamentoBase):
    Modificado: Optional[datetime] = None

class PuestoDepartamento(PuestoDepartamentoBase):
    PuestoID: int
    Creado: datetime
    Modificado: Optional[datetime] = None

    class Config:
        orm_mode = True
