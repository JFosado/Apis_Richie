import models.personal_medico
import schemas.personal_medico
from sqlalchemy.orm import Session




def get_personalMedico_by_ID(db: Session, Persona_ID: int):
    return db.query(models.personal_medico.PersonalMedico).filter(models.personal_medico.PersonalMedico.Persona_ID == Persona_ID).first()

def get_all_personal_medico(db: Session, skip:int=0,limit:int=10):
    return db.query(models.personal_medico.PersonalMedico).offset(skip).limit(limit).all()



def create_personal_medico(db: Session, personalMedico: schemas.personal_medico.PersonalMedicoCreate):
    db_personal_medico = models.personal_medico.PersonalMedico(
        Persona_ID=personalMedico.Persona_ID,  # Debes asegurarte de que este campo sea proporcionado o se maneje de manera apropiada
        Departamento_ID=personalMedico.Departamento_ID,
        Cedula_Profesional=personalMedico.Cedula_Profesional,
        Tipo=personalMedico.Tipo,
        Especialidad=personalMedico.Especialidad,
        Fecha_Registro=personalMedico.Fecha_Registro,
        Fecha_Contratacion=personalMedico.Fecha_Contratacion,
        Fecha_Termino_Contrato=personalMedico.Fecha_Termino_Contrato,
        Salario=personalMedico.Salario,
        Estatus=personalMedico.Estatus,
        Fecha_Actualizacion=personalMedico.Fecha_Actualizacion
    )
    db.add(db_personal_medico)
    db.commit()
    db.refresh(db_personal_medico)
    return db_personal_medico

def update_personal_medico(db: Session, Persona_ID: int, personal_medico: schemas.personal_medico.PersonalMedicoUpdate):
    db_personal_medico = db.query(models.personal_medico.PersonalMedico).filter(models.personal_medico.PersonalMedico.Persona_ID == Persona_ID).first()
    if db_personal_medico:
        for var, value in vars(personal_medico).items():
            setattr(db_personal_medico, var, value) if value else None
        db.commit()
        db.refresh(db_personal_medico)
    return db_personal_medico

def delete_personal_medico(db: Session, Persona_ID: int):
    db_personal_medico = db.query(models.personal_medico.PersonalMedico).filter(models.personal_medico.PersonalMedico.Persona_ID == Persona_ID).first()
    if  db_personal_medico:
        db.delete(db_personal_medico)
        db.commit()
    return db_personal_medico

