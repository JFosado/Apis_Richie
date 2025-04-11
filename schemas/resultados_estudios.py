from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class ResultadosEstudiosBase(BaseModel):
    Paciente_ID: int
    Personal_Medico_ID: int
    Estudio_ID: int
    Folio: str
    Resultados: str
    Observaciones: str
    Estatus: Optional[str] = None
    Fecha_Registro: datetime
    Fecha_Actualizacion: Optional[datetime] = None

class ResultadosEstudiosCreate(ResultadosEstudiosBase):
    pass

class ResultadosEstudiosUpdate(ResultadosEstudiosBase):
    pass

class ResultadosEstudios(ResultadosEstudiosBase):
    id: int

    class Config:
        orm_mode = True
