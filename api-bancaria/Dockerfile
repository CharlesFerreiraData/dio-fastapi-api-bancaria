# Usa uma imagem leve do Python
FROM python:3.10-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de dependências para o container
COPY requirements.txt .

# Instala as bibliotecas necessárias
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o conteúdo da sua pasta local para o container
COPY . .

# Expõe a porta padrão do FastAPI
EXPOSE 8000

# Comando para rodar a API (usando 0.0.0.0 para ser acessível fora do container)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]