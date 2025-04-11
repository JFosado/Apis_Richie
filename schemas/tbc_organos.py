from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class AparatoSistemaEnum(str, Enum):
    Circulatorio = 'Circulatorio'
    Digestivo = 'Digestivo'
    Respiratorio = 'Respiratorio'
    Nervioso = 'Nervioso'
    Muscular = 'Muscular'
    Esqueletico = 'Esquelético'
    Endocrino = 'Endocrino'
    Linfatico = 'Linfático'
    Inmunologico = 'Inmunológico'
    Reproductor = 'Reproductor'
    Urinario = 'Urinario'
    Sensorial = 'Sensorial'

class DisponibilidadEnum(str, Enum):
    EnProceso = 'En Proceso'
    Disponible = 'Disponible'
    NoDisponible = 'No Disponible'
    Reservado = 'Reservado'
    Entregado = 'Entregado'

class TipoEnum(str, Enum):
    Vital = 'Vital'
    NoVital = 'No Vital'

class GrupoSanguineoEnum(str, Enum):
    APos = 'A+'
    ANeg = 'A-'
    BPos = 'B+'
    BNeg = 'B-'
    ABPos = 'AB+'
    ABNeg = 'AB-'
    OPos = 'O+'
    ONeg = 'O-'

class EstadoSaludEnum(str, Enum):
    Excelente = 'Excelente'
    Bueno = 'Bueno'
    Regular = 'Regular'
    Pobre = 'Pobre'
    Critico = 'Crítico'

class OrganoBase(BaseModel):
    Nombre: str
    Aparato_Sistema: AparatoSistemaEnum
    Detalles_Adicionales: str
    Disponibilidad: DisponibilidadEnum
    Tipo: TipoEnum
    Fecha_Extraccion: datetime | None = None
    Edad_Donante: int | None = None
    Grupo_Sanguineo: GrupoSanguineoEnum
    Estado_Salud: EstadoSaludEnum
    Enfermedades_Transmisibles: bool
    Estatus: bool

class OrganoCreate(OrganoBase):
    pass

class OrganoUpdate(OrganoBase):
    pass

class Organo(OrganoBase):
    ID: int
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime

    class Config:
        from_attributes = True