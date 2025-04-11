from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.resultadosEstudios, config.db, schemas.resultadosEstudios, models.resultadosEstudios
from typing import List
from jwt_config import solicita_token
from portadortoken import Portador

resultadosEstudios = APIRouter()

models.resultadosEstudios.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@resultadosEstudios.get("/resultados_estudios/", response_model=List[schemas.resultadosEstudios.ResultadosEstudios], tags=["Resultados Estudios"], dependencies=[Depends(Portador())])
def read_resultados_estudios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_resultados_estudios = crud.resultadosEstudios.get_resultados_estudios(db=db, skip=skip, limit=limit)
    return db_resultados_estudios

@resultadosEstudios.get("/resultado_estudio/{id}", response_model=schemas.resultadosEstudios.ResultadosEstudios, tags=["Resultados Estudios"], dependencies=[Depends(Portador())])
def read_resultado_estudio(id: int, db: Session = Depends(get_db)):
    db_resultado_estudio = crud.resultadosEstudios.get_resultado_estudio(db=db, id=id)
    if db_resultado_estudio is None:
        raise HTTPException(status_code=404, detail="Resultado de estudio no encontrado")
    return db_resultado_estudio

@resultadosEstudios.post("/resultado_estudio/", response_model=schemas.resultadosEstudios.ResultadosEstudios, tags=["Resultados Estudios"])
def create_resultado_estudio(resultado_estudio: schemas.resultadosEstudios.ResultadosEstudiosCreate, db: Session = Depends(get_db)):
    return crud.resultadosEstudios.create_resultado_estudio(db=db, resultado_estudio=resultado_estudio)

@resultadosEstudios.put("/resultado_estudio/{id}", response_model=schemas.resultadosEstudios.ResultadosEstudios, tags=["Resultados Estudios"], dependencies=[Depends(Portador())])
def update_resultado_estudio(id: int, resultado_estudio: schemas.resultadosEstudios.ResultadosEstudiosUpdate, db: Session = Depends(get_db)):
    db_resultado_estudio = crud.resultadosEstudios.update_resultado_estudio(db=db, id=id, resultado_estudio=resultado_estudio)
    if db_resultado_estudio is None:
        raise HTTPException(status_code=404, detail="Resultado de estudio no existe, no actualizado")
    return db_resultado_estudio

@resultadosEstudios.delete("/resultado_estudio/{id}", response_model=schemas.resultadosEstudios.ResultadosEstudios, tags=["Resultados Estudios"], dependencies=[Depends(Portador())])
def delete_resultado_estudio(id: int, db: Session = Depends(get_db)):
    db_resultado_estudio = crud.resultadosEstudios.delete_resultado_estudio(db=db, id=id)
    if db_resultado_estudio is None:
        raise HTTPException(status_code=404, detail="Resultado de estudio no existe, no se pudo eliminar")
    return db_resultado_estudio
