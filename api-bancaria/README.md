# 🏦 API Bancária Assíncrona com FastAPI

Este projeto é uma solução para o desafio de criar uma API para um sistema bancário utilizando **FastAPI**, focando em operações assíncronas e validação de dados com **Pydantic**. 

O sistema permite a gestão de clientes, criação de contas e operações de depósito, seguindo os princípios de Programação Orientada a Objetos (POO).

## 🚀 Tecnologias Utilizadas
* **Python 3.10+** (Instalado via Anaconda/Conda)
* **FastAPI**: Framework web moderno e de alta performance.
* **Uvicorn**: Servidor ASGI para rodar a aplicação.
* **Pydantic**: Para validação de schemas e tipos de dados.

## 📂 Estrutura do Projeto
* `app/`: Contém a lógica da aplicação (`main.py`, `database.py`, `schemas.py`).
* `docs_screenshots/`: Evidências da API em funcionamento.
* `requirements.txt`: Lista de dependências do projeto.
* `.gitignore`: Filtro de arquivos para o Git.
* `Dockerfile`: Configuração para containerização da API.

## 🛠️ Como Executar o Projeto

1. **Instalar as dependências** (Via Anaconda Prompt ou PowerShell):
   ```bash
   pip install fastapi uvicorn pydantic