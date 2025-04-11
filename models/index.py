# index.py

from config.db import engine, Base

# Importa tus modelos aquí en orden lógico
from models.persons import Person
from models.paciente import Paciente
from models.users import User
from models.departamentos import Departamentos
from models.personal_medico import PersonalMedico
from models.areas_medicas import AreaMedica
from models.espacios import Espacio
from models.medicamentos import Medicamento
from models.servicios_medicos import ServiceM
from models.consumibles import Consumible
from models.servicios_medicos_consumibles import ServiciosMedicosConsumibles
from models.servicios_medicos_espacios import ServiciosMedicosEspacios
from models.citas import CitaMedica
from models.receta import Receta
from models.dispensaciones import Dispensacion
from models.lotes_medicamentos import LoteMedicamento
from models.solicitudes import Solicitud
from models.rols import Rol
from models.usersrols import UserRol
from models.bitacora import Bitacora
from models.cirugias import Cirugia
from models.especialidades import Especialidad
from models.estudios import Estudios
from models.expediente import Expediente
from models.horarios import Horario
from models.personal import Personal
from models.puestos import Puesto
from models.puestos_departamentos import PuestoDepartamento
from models.resultados_estudios import ResultadosEstudios
from models.tbb_aprobaciones import Aprobaciones
from models.tbc_organos import Organo

# Si tienes otros modelos intermedios, agrégalos aquí:
# from models.servicios_medicos_consumibles import ServiciosMedicosConsumibles
# from models.servicios_medicos_espacios import ServiciosMedicosEspacios

# Definir qué se exporta al importar desde src.models
__all__ = [
    "Person",
    "Paciente",
    "User",
    "Departamentos",
    "PersonalMedico",
    "AreaMedica",
    "Espacio",
    "Medicamento",
    "ServiceM",
    "Consumible",
    "ServiciosMedicosConsumibles",
    "ServiciosMedicosEspacios",
    "CitaMedica",
    "Receta",
    "Dispensacion",
    "LoteMedicamento",
    "Solicitud",
    "Rol",
    "UserRol",
    "Bitacora",
    "Cirugia",
    "Especialidad",
    "Estudios",
    "Expediente",
    "Horario",
    "Personal",
    "Puesto",
    "PuestoDepartamento",
    "ResultadosEstudios",
    "Aprobaciones",
    "Organo"
]
