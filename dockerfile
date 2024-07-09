# DOCKERFILE............................
# Use uma imagem base do Ubuntu 22.04
FROM ubuntu:22.04

# Atualize o sistema e instale dependências
RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-pip \
    libpq-dev # Dependência para psycopg2-binary

# Instalar psycopg2-binary para PostgreSQL
RUN pip3 install psycopg2-binary

# Instalar py-trello para integração com o Trello
RUN pip3 install py-trello

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o código-fonte para o contêiner
COPY app.py .
# Copiar arquivo .env para o conteiner
COPY .env .  




