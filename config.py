import json

# Загрузка конфигурационных данных из config.json
with open('config.json', 'r') as f:
    config = json.load(f)

TOKEN = config['TOKEN']
SERVERS_FILE_TEMPLATE = config['SERVERS_FILE_TEMPLATE']
DEFAULT_SERVER = config['DEFAULT_SERVER']
MAX_SERVERS = 10  # Максимальное количество серверов