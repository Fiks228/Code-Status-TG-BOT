import json
import os
import random

def load_servers(chat_id, template, default_server):
    filename = template.format(chat_id=chat_id)
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    else:
        return default_server.copy()

def save_servers(chat_id, servers, template):
    filename = template.format(chat_id=chat_id)
    with open(filename, 'w') as f:
        json.dump(servers, f, indent=4)

def generate_unique_id(existing_ids):
    while True:
        new_id = str(random.randint(1, 99999))
        if new_id not in existing_ids:
            return new_id