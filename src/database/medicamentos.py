from sqlalchemy.orm import Session

from . import models, schema


def get_medicamentos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Medicamento).offset(skip).limit(limit).all()


def get_medicamento(db: Session, medicamento_id: int):
    return (
        db.query(models.Medicamento)
        .filter(models.Medicamento.id == medicamento_id)
        .first()
    )


def create_medicamento(db: Session, medicamento: schema.MedicamentoCreate):
    db_medicamento = models.Medicamento(**medicamento.model_dump())
    db.add(db_medicamento)
    db.commit()
    db.refresh(db_medicamento)
    return db_medicamento


def update_medicamento(
    db: Session, medicamento_id: int, medicamento: schema.MedicamentoCreate
):
    db_medicamento = get_medicamento(db, medicamento_id)
    if db_medicamento:
        for key, value in medicamento.model_dump().items():
            setattr(db_medicamento, key, value)
        db.commit()
        db.refresh(db_medicamento)
    return db_medicamento


def delete_medicamento(db: Session, medicamento_id: int):
    db_medicamento = get_medicamento(db, medicamento_id)
    if db_medicamento:
        db.delete(db_medicamento)
        db.commit()
    return db_medicamento
