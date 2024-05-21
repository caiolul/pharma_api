from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String

from . import Base


class Medicamento(Base):
    __tablename__ = "medicamentos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    descricao = Column(String)
    fabricante = Column(String)
    data_validade = Column(Date)
    preco = Column(Float)
    quantidade_estoque = Column(Integer)


class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    endereco = Column(String)
    telefone = Column(String)
    email = Column(String)


class Prescricao(Base):
    __tablename__ = "prescricoes"
    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id", ondelete="CASCADE"))
    medicamento_id = Column(Integer, ForeignKey("medicamentos.id"))
    quantidade = Column(Integer)
    data_prescricao = Column(Date)


class Fornecedor(Base):
    __tablename__ = "fornecedores"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    contato = Column(String)
    produto_fornecido = Column(String)
