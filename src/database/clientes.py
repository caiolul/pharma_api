from sqlalchemy.orm import Session

from . import models, schema


def get_clients(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Cliente).offset(skip).limit(limit).all()


def get_client(db: Session, client_id: int):
    return db.query(models.Cliente).filter(models.Cliente.id == client_id).first()


def create_client(db: Session, client: schema.ClienteCreate):
    db_client = models.Cliente(**client.model_dump())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


def update_client(db: Session, client_id: int, client: schema.ClienteCreate):
    db_client = get_client(db, client_id)
    if db_client:
        for key, value in client.model_dump().items():
            setattr(db_client, key, value)
        db.commit()
        db.refresh(db_client)
    return db_client


def delete_client(db: Session, client_id: int):
    db_client = get_client(db, client_id)
    if db_client:
        db.delete(db_client)
        db.commit()
    return db_client
