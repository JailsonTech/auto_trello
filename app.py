# app.py

from trello import TrelloClient
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obter chaves do arquivo .env para o Trello
TRELLO_API_KEY = os.getenv('TRELLO_API_KEY')
TRELLO_TOKEN = os.getenv('TRELLO_TOKEN')
TRELLO_CARD_ID = os.getenv('TRELLO_CARD_ID')

# Inicializar cliente do Trello
client = TrelloClient(
    api_key=TRELLO_API_KEY,
    token=TRELLO_TOKEN
)

# Obter o cartão do Trello
card = client.get_card(TRELLO_CARD_ID)

# Exibir informações do cartão
print(f'Nome do cartão: {card.name}')
print(f'Descrição do cartão: {card.description}')
print(f'ID do cartão: {card.id}')
print(f'URL do cartão: {card.shortUrl}')
