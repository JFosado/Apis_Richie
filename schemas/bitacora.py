from pydantic import BaseModel
from datetime import datetime
from typing import Optional
import enum
from datetime import datetime,timezone


class OP(str, enum.Enum):
    Create = "Create"
    Read = "Read"
    Update = "Update"
    Delete = "Delete"

class BitacoraBase(BaseModel):
    Usuario: str
    Operacion: OP
    Tabla: str
    Descripcion: str
    Estatus: Optional[bool] = True
    Fecha_Registro: Optional[datetime] = None

class BitacoraCreate(BitacoraBase):
    Fecha_Registro: datetime = datetime.utcnow()  # Valor por defecto

class BitacoraUpdate(BaseModel):
    Usuario: Optional[str]
    Operacion: Optional[OP]
    Tabla: Optional[str]
    Descripcion: Optional[str]
    Estatus: Optional[bool]
    Fecha_Registro: Optional[datetime]

class Bitacora(BitacoraBase):
    ID: int
    #owner_id: int clave foranea
    class Config:
        from_attributes= True
        
# class UserLogin(BaseModel):
#     usuario: str
#     password: str
