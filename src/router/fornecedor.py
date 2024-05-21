from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import fornecedores as fornecedor_db
from database import get_db
from database import schema as schemas_fornecedor

router = APIRouter()


@router.post("/fornecedor/", response_model=schemas_fornecedor.Fornecedor)
def create_fornecedor(
    fornecedor: schemas_fornecedor.FornecedorCreate, db: Session = Depends(get_db)
):
    return fornecedor_db.create_fornecedor(db=db, fornecedor=fornecedor)


@router.get("/fornecedor/", response_model=list[schemas_fornecedor.Fornecedor])
def list_fornecedores(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return fornecedor_db.get_fornecedores(db, skip=skip, limit=limit)


@router.get("/fornecedor/{fornecedor_id}", response_model=schemas_fornecedor.Fornecedor)
def read_fornecedor(fornecedor_id: int, db: Session = Depends(get_db)):
    db_fornecedor = fornecedor_db.get_fornecedor(db, fornecedor_id=fornecedor_id)
    if db_fornecedor is None:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    return db_fornecedor


@router.put("/fornecedor/{fornecedor_id}", response_model=schemas_fornecedor.Fornecedor)
def update_fornecedor(
    fornecedor_id: int,
    fornecedor: schemas_fornecedor.FornecedorCreate,
    db: Session = Depends(get_db),
):
    return fornecedor_db.update_fornecedor(
        db=db, fornecedor_id=fornecedor_id, fornecedor=fornecedor
    )


@router.delete("/fornecedor/{fornecedor_id}")
def delete_fornecedor(fornecedor_id: int, db: Session = Depends(get_db)):
    fornecedor_db.delete_fornecedor(db, fornecedor_id)
    return {"detail": "Fornecedor deletado"}
