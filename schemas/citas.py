from typing import List,Union
from pydantic import BaseModel
from datetime import datetime

from models.citas import MyEstatusCita

class CitasBase(BaseModel):
    Persona_ID: int
    Hora_Cita:datetime
    Telefono:str
    Correo_Electronico:str
    Motivo_Cita:str
    Estatus:MyEstatusCita
    
    
class CitasCreate(CitasBase):
    pass
class CitasUpdate(CitasBase):
    pass
class Citas(CitasBase):
    ID: int
    Persona_ID: int
    class Config:
        orm_mode = True