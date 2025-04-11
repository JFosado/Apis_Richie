from sqlalchemy.orm import Session
import models.resultadosEstudios
import schemas.resultadosEstudios

def get_resultado_estudio(db: Session, id: int):
    return db.query(models.resultadosEstudios.ResultadosEstudios).filter(models.resultadosEstudios.ResultadosEstudios.ID == id).first()

def get_resultadosEstudios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.resultadosEstudios.ResultadosEstudios).offset(skip).limit(limit).all()

def create_resultado_estudio(db: Session, resultado_estudio: schemas.resultadosEstudios.ResultadosEstudiosCreate):
    db_resultado_estudio = models.resultadosEstudios.ResultadosEstudios(
        #Paciente_ID=resultado_estudio.Paciente_ID,
        #Personal_Medico_ID=resultado_estudio.Personal_Medico_ID,
        #Estudio_ID=resultado_estudio.Estudio_ID,
        Folio=resultado_estudio.Folio,
        Resultados=resultado_estudio.Resultados,
        Observaciones=resultado_estudio.Observaciones,
        Estatus=resultado_estudio.Estatus,
        Fecha_Registro=resultado_estudio.Fecha_Registro,
        Fecha_Actualizacion=resultado_estudio.Fecha_Actualizacion,
    )
    db.add(db_resultado_estudio)
    db.commit()
    db.refresh(db_resultado_estudio)
    return db_resultado_estudio

def update_resultado_estudio(db: Session, id: int, resultado_estudio: schemas.resultadosEstudios.ResultadosEstudiosUpdate):
    db_resultado_estudio = db.query(models.resultadosEstudios.ResultadosEstudios).filter(models.resultadosEstudios.ResultadosEstudios.ID == id).first()
    if db_resultado_estudio:
        for var, value in vars(resultado_estudio).items():
            setattr(db_resultado_estudio, var, value) if value else None
        db.commit()
        db.refresh(db_resultado_estudio)
    return db_resultado_estudio

def delete_resultado_estudio(db: Session, id: int):
    db_resultado_estudio = db.query(models.resultadosEstudios.ResultadosEstudios).filter(models.resultadosEstudios.ResultadosEstudios.ID == id).first()
    if db_resultado_estudio:
        db.delete(db_resultado_estudio)
        db.commit()
    return db_resultado_estudio
