from pydantic import BaseModel
from datetime import datetime
from typing import Optional
import enum

# Enum para operaciones CRUD
class OP(str, enum.Enum):
    Create = "Create"
    Read = "Read"
    Update = "Update"
    Delete = "Delete"

# Esquema base común
class BitacoraBase(BaseModel):
    Usuario: str
    Operacion: OP
    Tabla: str
    Descripcion: str
    Estatus: Optional[bool] = True
    Fecha_Registro: Optional[datetime] = None

# Para creación, asigna fecha por defecto si no se pasa
class BitacoraCreate(BitacoraBase):
    Fecha_Registro: datetime = datetime.utcnow()

# Para actualizaciones, todos los campos son opcionales
class BitacoraUpdate(BaseModel):
    Usuario: Optional[str]
    Operacion: Optional[OP]
    Tabla: Optional[str]
    Descripcion: Optional[str]
    Estatus: Optional[bool]
    Fecha_Registro: Optional[datetime]

# Para respuesta o uso interno (por ejemplo en consultas)
class Bitacora(BitacoraBase):
    ID: int
    #owner_id: int  # si en algún momento agregan relaciones
    class Config:
        from_attributes = True

# --- Si existen más versiones como Bitacora1, BitacoraDetailed, etc., colócalas aquí ---

# class UserLogin(BaseModel):  # Comentado por si en el futuro se usa
#     usuario: str
#     password: str
