from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from database import prescricoes as prescricao_db
from database import schema as schemas_prescricao

router = APIRouter()


@router.post("/prescricao/", response_model=schemas_prescricao.Prescricao)
def create_prescricao(
    prescricao: schemas_prescricao.PrescricaoCreate, db: Session = Depends(get_db)
):
    return prescricao_db.create_prescricao(db=db, prescricao=prescricao)


@router.get("/prescricao/", response_model=list[schemas_prescricao.Prescricao])
def list_prescricoes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return prescricao_db.get_prescricoes(db, skip=skip, limit=limit)


@router.get("/prescricao/{prescricao_id}", response_model=schemas_prescricao.Prescricao)
def read_prescricao(prescricao_id: int, db: Session = Depends(get_db)):
    db_prescricao = prescricao_db.get_prescricao(db, prescricao_id=prescricao_id)
    if db_prescricao is None:
        raise HTTPException(status_code=404, detail="Prescricao não encontrado")
    return db_prescricao


@router.put("/prescricao/{prescricao_id}", response_model=schemas_prescricao.Prescricao)
def update_prescricao(
    prescricao_id: int,
    prescricao: schemas_prescricao.PrescricaoCreate,
    db: Session = Depends(get_db),
):
    return prescricao_db.update_prescricao(
        db=db, prescricao_id=prescricao_id, prescricao=prescricao
    )


@router.delete("/prescricao/{prescricao_id}")
def delete_prescricao(prescricao_id: int, db: Session = Depends(get_db)):
    prescricao_db.delete_prescricao(db, prescricao_id)
    return {"detail": "Prescricao deletado"}
