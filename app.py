# app.py

from trello import TrelloClient
import os
from dotenv import load_dotenv
from datetime import datetime
import pytz


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
print(f'\nNome do cartão: {card.name}')
print(f'Descrição do cartão: {card.description}')
print(f'URL do cartão: {card.shortUrl}')

# Definir o fuso horário de Salvador
salvador_timezone = pytz.timezone('America/Bahia')

# Mostrar a data do cartão, se existir
if card.due_date:
    if isinstance(card.due_date, datetime):
        due_date_salvador = card.due_date.astimezone(salvador_timezone)
    else:
        due_date_utc = datetime.strptime(card.due_date, '%Y-%m-%dT%H:%M:%S.%fZ')
        due_date_utc = due_date_utc.replace(tzinfo=pytz.utc)
        due_date_salvador = due_date_utc.astimezone(salvador_timezone)
    
    formatted_due_date = due_date_salvador.strftime('%d/%m/%Y')
    print(f'Data do cartão: {formatted_due_date}')
else:
    print('Este cartão não possui uma data definida.')
    
# Verificar se há checklists no cartão
if card.checklists:
    # Iterar sobre os checklists do cartão
    print("\n.............CHECKLISTS.............")
    for checklist in card.checklists:
        # Contar o número de itens no checklist
        num_items = len(checklist.items)
        print()
        print(f'{checklist.name.upper()} - Total de itens: {num_items}')        
        # Exibir os itens do checklist
        for item in checklist.items:
            print(f' - {item["name"]} ({item["state"]})')
else:
    print('Este cartão não possui nenhum checklist.')









