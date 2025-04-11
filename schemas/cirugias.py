from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

# Enum types for Nivel_Urgencia and Estatus
class NivelUrgenciaEnum(str, Enum):
    Bajo = "Bajo"
    Medio = "Medio"
    Alto = "Alto"

class EstatusEnum(str, Enum):
    Programada = "Programada"
    EnCurso = "En curso"
    Completada = "Completada"
    Cancelada = "Cancelada"

class CirugiaBase(BaseModel):
    Paciente_ID: int
    Espacio_Medico_ID: int
    Tipo: str
    Nombre: str
    Descripcion: str
    Nivel_Urgencia: NivelUrgenciaEnum
    Horario: datetime
    Observaciones: Optional[str] = None
    Valoracion_Medica: Optional[str] = None
    Estatus: EstatusEnum
    Consumible: str
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime

class CirugiaCreate(CirugiaBase):
    pass

class CirugiaUpdate(CirugiaBase):
    pass

class Cirugia(CirugiaBase):
    ID: int
    class Config:
        orm_mode = True 
