from sqlalchemy.orm import Session
import models.resultados_estudios
import schemas.resultados_estudios

def get_resultado_estudio(db: Session, id: int):
    return db.query(models.resultados_estudios.ResultadosEstudios).filter(models.resultados_estudios.ResultadosEstudios.id == id).first()

def get_resultados_estudios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.resultados_estudios.ResultadosEstudios).offset(skip).limit(limit).all()

def create_resultado_estudio(db: Session, resultado_estudio: schemas.resultados_estudios.ResultadosEstudiosCreate):
    db_resultado_estudio = models.resultados_estudios.ResultadosEstudios(
        Paciente_ID=resultado_estudio.Paciente_ID,
        Personal_Medico_ID=resultado_estudio.Personal_Medico_ID,
        Estudio_ID=resultado_estudio.Estudio_ID,
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

def update_resultado_estudio(db: Session, id: int, resultado_estudio: schemas.resultados_estudios.ResultadosEstudiosUpdate):
    db_resultado_estudio = db.query(models.resultados_estudios.ResultadosEstudios).filter(models.resultados_estudios.ResultadosEstudios.id == id).first()
    if db_resultado_estudio:
        for var, value in vars(resultado_estudio).items():
            setattr(db_resultado_estudio, var, value) if value else None
        db.commit()
        db.refresh(db_resultado_estudio)
    return db_resultado_estudio

def delete_resultado_estudio(db: Session, id: int):
    db_resultado_estudio = db.query(models.resultados_estudios.ResultadosEstudios).filter(models.resultados_estudios.ResultadosEstudios.id == id).first()
    if db_resultado_estudio:
        db.delete(db_resultado_estudio)
        db.commit()
    return db_resultado_estudio
