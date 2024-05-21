from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from database import medicamentos as med
from database import schema as schemas_med

router = APIRouter()


@router.post("/medicamentos/", response_model=schemas_med.Medicamento)
def create_medicamento(
    medicamento: schemas_med.MedicamentoCreate, db: Session = Depends(get_db)
):
    return med.create_medicamento(db=db, medicamento=medicamento)


@router.get("/medicamentos/", response_model=list[schemas_med.Medicamento])
def read_medicamentos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return med.get_medicamentos(db, skip=skip, limit=limit)


@router.get("/medicamentos/{medicamento_id}", response_model=schemas_med.Medicamento)
def read_medicamento(medicamento_id: int, db: Session = Depends(get_db)):
    db_medicamento = med.get_medicamento(db, medicamento_id=medicamento_id)
    if db_medicamento is None:
        raise HTTPException(status_code=404, detail="Medicamento não encontrado")
    return db_medicamento


@router.put("/medicamentos/{medicamento_id}", response_model=schemas_med.Medicamento)
def update_medicamento(
    medicamento_id: int,
    medicamento: schemas_med.MedicamentoCreate,
    db: Session = Depends(get_db),
):
    return med.update_medicamento(db, medicamento_id, medicamento)


@router.delete("/medicamentos/{medicamento_id}")
def delete_medicamento(medicamento_id: int, db: Session = Depends(get_db)):
    med.delete_medicamento(db, medicamento_id)
    return {"detail": "Medicamento deletado"}
