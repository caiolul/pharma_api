from sqlalchemy.orm import Session

from . import models, schema


def get_prescricoes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Prescricao).offset(skip).limit(limit).all()


def get_prescricao(db: Session, prescricao_id: int):
    return (
        db.query(models.Prescricao)
        .filter(models.Prescricao.id == prescricao_id)
        .first()
    )


def create_prescricao(db: Session, prescricao: schema.PrescricaoCreate):
    db_prescricao = models.Prescricao(**prescricao.model_dump())
    db.add(db_prescricao)
    db.commit()
    db.refresh(db_prescricao)
    return db_prescricao


def update_prescricao(
    db: Session, prescricao_id: int, prescricao: schema.PrescricaoCreate
):
    db_prescricao = get_prescricao(db, prescricao_id)
    if db_prescricao:
        for key, value in prescricao.model_dump().items():
            setattr(db_prescricao, key, value)
        db.commit()
        db.refresh(db_prescricao)
    return db_prescricao


def delete_prescricao(db: Session, prescricao_id: int):
    db_prescricao = get_prescricao(db, prescricao_id)
    if db_prescricao:
        db.delete(db_prescricao)
        db.commit()
    return db_prescricao
