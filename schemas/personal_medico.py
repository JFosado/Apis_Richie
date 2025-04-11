from typing import List,Union
from pydantic import BaseModel, Field
from datetime import datetime
from decimal import Decimal
from models.personal_medico import EnumTipoPersonal, EnumEstatus


class PersonalMedicoBase(BaseModel):
    Persona_ID: int
    Departamento_ID: int
    Cedula_Profesional: str
    Tipo: EnumTipoPersonal
    Especialidad: str
    Fecha_Registro: datetime
    Fecha_Contratacion: datetime
    Fecha_Termino_Contrato : datetime 
    Salario: Decimal
    Estatus: EnumEstatus
    Fecha_Actualizacion: datetime 

    
    
class PersonalMedicoCreate(PersonalMedicoBase):
    pass
class PersonalMedicoUpdate(PersonalMedicoBase):
    pass
class PersonalMedico(PersonalMedicoBase):
    Persona_ID: int

    class Config:
        orm_mode = True