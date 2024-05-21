from fastapi import FastAPI
from router.medicamentos import router as medicamentos_router
from router.clientes import router as clientes_router
from database import models
from database import engine

app = FastAPI()
models.Base.metadata.create_all(bind=engine)
app.include_router(medicamentos_router, tags=["medicamentos"])
app.include_router(clientes_router, tags=["clientes"])
