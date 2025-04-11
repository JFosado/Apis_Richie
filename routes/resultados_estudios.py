from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.resultados_estudios, config.db, schemas.resultados_estudios, models.resultados_estudios
from typing import List
from jwt_config import solicita_token
from portadortoken import Portador

resultados_estudios = APIRouter()

models.resultados_estudios.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@resultados_estudios.get("/resultados_estudios/", response_model=List[schemas.resultados_estudios.ResultadosEstudios], tags=["ResultadosEstudios"], dependencies=[Depends(Portador())])
def read_resultados_estudios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_resultados_estudios = crud.resultados_estudios.get_resultados_estudios(db=db, skip=skip, limit=limit)
    return db_resultados_estudios

@resultados_estudios.get("/resultados_estudios/{id}", response_model=schemas.resultados_estudios.ResultadosEstudios, tags=["ResultadosEstudios"], dependencies=[Depends(Portador())])
def read_resultado_estudio(id: int, db: Session = Depends(get_db)):
    db_resultado_estudio = crud.resultados_estudios.get_resultado_estudio(db=db, id=id)
    if db_resultado_estudio is None:
        raise HTTPException(status_code=404, detail="Resultado del estudio no encontrado")
    return db_resultado_estudio

@resultados_estudios.post("/resultados_estudios/", response_model=schemas.resultados_estudios.ResultadosEstudios, tags=["ResultadosEstudios"])
def create_resultado_estudio(resultado_estudio: schemas.resultados_estudios.ResultadosEstudiosCreate, db: Session = Depends(get_db)):
    return crud.resultados_estudios.create_resultado_estudio(db=db, resultado_estudio=resultado_estudio)

@resultados_estudios.put("/resultados_estudios/{id}", response_model=schemas.resultados_estudios.ResultadosEstudios, tags=["ResultadosEstudios"], dependencies=[Depends(Portador())])
def update_resultado_estudio(id: int, resultado_estudio: schemas.resultados_estudios.ResultadosEstudiosUpdate, db: Session = Depends(get_db)):
    db_resultado_estudio = crud.resultados_estudios.update_resultado_estudio(db=db, id=id, resultado_estudio=resultado_estudio)
    if db_resultado_estudio is None:
        raise HTTPException(status_code=404, detail="Resultado del estudio no existe, no actualizado")
    return db_resultado_estudio

@resultados_estudios.delete("/resultados_estudios/{id}", response_model=schemas.resultados_estudios.ResultadosEstudios, tags=["ResultadosEstudios"], dependencies=[Depends(Portador())])
def delete_resultado_estudio(id: int, db: Session = Depends(get_db)):
    db_resultado_estudio = crud.resultados_estudios.delete_resultado_estudio(db=db, id=id)
    if db_resultado_estudio is None:
        raise HTTPException(status_code=404, detail="Resultado del estudio no existe, no se pudo eliminar")
    return db_resultado_estudio
