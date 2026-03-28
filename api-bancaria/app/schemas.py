from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class TransacaoSchema(BaseModel):
    tipo: str
    valor: float
    data: str = Field(default_factory=lambda: datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

class ContaSchema(BaseModel):
    numero: int
    agencia: str = "0001"
    saldo: float = 0.0
    historico: List[TransacaoSchema] = []

class ClienteSchema(BaseModel):
    cpf: str
    nome: str
    contas: List[ContaSchema] = []