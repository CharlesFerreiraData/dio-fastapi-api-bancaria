from fastapi import FastAPI, HTTPException
from .schemas import ClienteSchema, ContaSchema, TransacaoSchema
from .database import db_clientes

app = FastAPI(title="API Bancária Assíncrona - DIO")

@app.get("/")
async def root():
    return {"message": "Bem-vindo à API Bancária Assíncrona!"}

@app.post("/clientes/", status_code=201)
async def criar_cliente(cliente: ClienteSchema):
    if any(c.cpf == cliente.cpf for c in db_clientes):
        raise HTTPException(status_code=400, detail="CPF já cadastrado.")
    db_clientes.append(cliente)
    return {"message": "Cliente cadastrado com sucesso!"}

@app.post("/clientes/{cpf}/contas/", status_code=201)
async def criar_conta(cpf: str):
    cliente = next((c for c in db_clientes if c.cpf == cpf), None)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado.")
    
    nova_conta = ContaSchema(numero=len(cliente.contas) + 1)
    cliente.contas.append(nova_conta)
    return nova_conta

@app.post("/clientes/{cpf}/contas/{numero_conta}/depositar/")
async def depositar(cpf: str, numero_conta: int, valor: float):
    cliente = next((c for c in db_clientes if c.cpf == cpf), None)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado.")
    
    conta = next((ct for ct in cliente.contas if ct.numero == numero_conta), None)
    if not conta:
        raise HTTPException(status_code=404, detail="Conta não encontrada.")
    
    conta.saldo += valor
    conta.historico.append(TransacaoSchema(tipo="Depósito", valor=valor))
    return {"message": "Depósito realizado", "novo_saldo": conta.saldo}