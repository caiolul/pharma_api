from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import clientes as client
from database import get_db
from database import schema as schemas_client

router = APIRouter()


@router.post("/cliente/", response_model=schemas_client.Cliente)
def create_client(cliente: schemas_client.ClienteCreate, db: Session = Depends(get_db)):
    return client.create_client(db=db, client=cliente)


@router.get("/cliente/", response_model=list[schemas_client.Cliente])
def read_clients(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return client.get_clients(db, skip=skip, limit=limit)


@router.get("/cliente/{client_id}", response_model=schemas_client.Cliente)
def read_client(client_id: int, db: Session = Depends(get_db)):
    db_client = client.get_client(db, client_id=client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return db_client


@router.put("/cliente/{client_id}", response_model=schemas_client.Cliente)
def update_client(
    client_id: int, cliente: schemas_client.ClienteCreate, db: Session = Depends(get_db)
):
    return client.update_client(db=db, client_id=client_id, client=cliente)


@router.delete("/cliente/{client_id}")
def delete_client(client_id: int, db: Session = Depends(get_db)):
    client.delete_client(db, client_id)
    return {"detail": "Cliente deletado"}
