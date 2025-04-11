from typing import List, Union, Optional
from pydantic import BaseModel
from datetime import datetime
from models.solicitudes import MyEstatus, MyPrioridad

class SolicitudBase(BaseModel):
    Paciente_ID: int
    Medico_ID: int
    Servicio_ID: int
    Prioridad: MyPrioridad
    Descripcion: str
    Estatus: MyEstatus
    Estatus_Aprobacion: bool
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime

class SolicitudCreate(SolicitudBase):
    pass

class SolicitudUpdate(SolicitudBase):
    pass

class Solicitud(SolicitudBase):
    ID: int
    class Config:
        from_attributes = True