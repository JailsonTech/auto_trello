# Use uma imagem base do Ubuntu 22.04
FROM ubuntu:22.04

# Atualize o sistema e instale dependências
RUN apt-get update && \
    apt-get install -y \
    ca-certificates \
    python3 \
    python3-pip \
    libpq-dev # Dependência para psycopg2-binary

# Configurar os certificados SSL para o Python
RUN update-ca-certificates

# Instalar psycopg2-binary e certifi para PostgreSQL
RUN pip3 install --upgrade pip && \
    pip3 install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org certifi && \
    pip3 install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org psycopg2-binary

# Instalar py-trello e python-dotenv
RUN pip3 install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org py-trello python-dotenv

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o código-fonte para o contêiner
COPY app.py .
COPY .env .

# Comando padrão para executar o app.py
CMD ["python3", "app.py"]








