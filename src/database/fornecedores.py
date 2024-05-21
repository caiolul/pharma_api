from sqlalchemy.orm import Session

from . import models, schema


def get_fornecedores(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Fornecedor).offset(skip).limit(limit).all()


def get_fornecedor(db: Session, forcenedor_id: int):
    return (
        db.query(models.Fornecedor)
        .filter(models.Fornecedor.id == forcenedor_id)
        .first()
    )


def create_fornecedor(db: Session, fornecedor: schema.FornecedorCreate):
    db_fornecedor = models.Fornecedor(**fornecedor.model_dump())
    db.add(db_fornecedor)
    db.commit()
    db.refresh(db_fornecedor)
    return db_fornecedor


def update_fornecedor(
    db: Session, forcenedor_id: int, fornecedor: schema.FornecedorCreate
):
    db_fornecedor = get_fornecedor(db, forcenedor_id)
    if db_fornecedor:
        for key, value in fornecedor.model_dump().items():
            setattr(db_fornecedor, key, value)
        db.commit()
        db.refresh(db_fornecedor)
    return db_fornecedor


def delete_fornecedor(db: Session, forcenedor_id: int):
    db_fornecedor = get_fornecedor(db, forcenedor_id)
    if db_fornecedor:
        db.delete(db_fornecedor)
        db.commit()
    return db_fornecedor
