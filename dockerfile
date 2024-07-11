#..Dockerfile...

# imagem base do Ubuntu 22.04
 FROM ubuntu:22.04

 # Atualiza o sistema e instale dependências
 RUN apt-get update && \
     apt-get install -y \
     python3 \
     python3-pip \
     libpq-dev
 
 # Instalar psycopg2-binary, py-trello e python-dotenv
 RUN pip3 install --upgrade pip && \
     pip3 install psycopg2-binary py-trello python-dotenv
 
 # Definir o diretório de trabalho
 WORKDIR /app
 
 # Copiar o código-fonte para o contêiner
 COPY app.py .
 COPY .env .
 
 # Comando padrão para executar o app.py
 CMD ["python3", "app.py"]
 