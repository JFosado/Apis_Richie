from typing import List,Union
from pydantic import BaseModel
from datetime import datetime

class RecetaBase(BaseModel):
    
    Nombre: str 
    Fecha_Nacimiento: datetime
    Peso: str
    Talla:str
    Edad: str
    Presion_arterial: str
    Diagnostico: str
    Prescripcion_Medica: str



    
    
class RecetaCreate(RecetaBase):
    pass
class RecetaUpdate(RecetaBase):
    pass
class Receta(RecetaBase):
    ID: int
    class Config:
        orm_mode = True