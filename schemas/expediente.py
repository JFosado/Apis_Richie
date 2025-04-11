from typing import List,Union
from pydantic import BaseModel
from datetime import datetime
from models.expediente import MyEstatusExpediente

class ExpedienteBase(BaseModel):
    
    Persona_ID: int
    Hora_Consulta: datetime
    Diagnostico: str
    Tratamiento_Relacionado: str
    Observaciones: str
    Estatus:MyEstatusExpediente



    
    
class ExpedienteCreate(ExpedienteBase):
    pass
class ExpedienteUpdate(ExpedienteBase):
    pass
class Expediente(ExpedienteBase):
    ID: int
    Persona_ID: int
    class Config:
        orm_mode = True