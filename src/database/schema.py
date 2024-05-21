from datetime import date

from pydantic import BaseModel


class MedicamentoBase(BaseModel):
    nome: str
    descricao: str
    fabricante: str
    data_validade: date
    preco: float
    quantidade_estoque: int


class MedicamentoCreate(MedicamentoBase):
    pass


class Medicamento(MedicamentoBase):
    id: int

    class Config:
        orm_mode = True


class ClienteBase(BaseModel):
    nome: str
    endereco: str
    telefone: str
    email: str


class ClienteCreate(ClienteBase):
    pass


class Cliente(ClienteBase):
    id: int

    class Config:
        orm_mode = True


class PrescricaoBase(BaseModel):
    cliente_id: int
    medicamento_id: int
    quantidade: int
    data_prescricao: date


class PrescricaoCreate(PrescricaoBase):
    pass


class Prescricao(PrescricaoBase):
    id: int

    class Config:
        orm_mode = True


class FornecedorBase(BaseModel):
    nome: str
    contato: str
    produto_fornecido: str


class FornecedorCreate(FornecedorBase):
    pass


class Fornecedor(FornecedorBase):
    id: int

    class Config:
        orm_mode = True
