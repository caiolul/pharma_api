# Pharma API


## Api para gerenciar uma farmacia


### Endpoints

#### GET /medicamentos

Retorna todos os medicamentos cadastrados

#### GET /medicamentos/{id}

Retorna um medicamento pelo id

#### POST /medicamentos

Cadastra um medicamento

#### PUT /medicamentos/{id}

Atualiza um medicamento

#### DELETE /medicamentos/{id}

Deleta um medicamento

#### GET /fornececedor/

Retorna todos os fornecedores cadastrados

#### GET /fornecedor/{id}

Retorna um fornecedor pelo id

#### POST /fornecedor/

Cadastra um fornecedor

#### PUT /fornecedor/{id}

Atualiza um fornecedor

#### DELETE /fornecedor/{id}

Deleta um fornecedor

#### GET /cliente/

Retorna todos os clientes cadastrados

#### GET /cliente/{id}

Retorna um cliente pelo id

#### POST /cliente/

Cadastra um cliente

#### PUT /cliente/{id}

Atualiza um cliente

#### DELETE /cliente/{id}

Deleta um cliente

#### GET /prescricao/

Retorna todas as prescrições cadastradas

#### GET /prescricao/{id}

Retorna uma prescrição pelo id

#### POST /prescricao/

Cadastra uma prescrição

#### PUT /prescricao/{id}

Atualiza uma prescrição

#### DELETE /prescricao/{id}

Deleta uma prescrição



### Tecnologias utilizadas

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pytest
- Docker / Docker compose


### Models

#### Medicamento

```python
{
    nome: str
    descricao: str
    fabricante: str
    data_validade: date
    preco: float
    quantidade_estoque: int
}
```

#### Fornecedor

```python
{
    nome: str
    contato: str
    produto_fornecido: str
}
```

#### Cliente

```python
{
    nome: str
    endereco: str
    telefone: str
    email: str
}
```

#### Prescrição

```python
{
    cliente_id: int
    medicamento_id: int
    quantidade: int
    data_prescricao: date
}
```
