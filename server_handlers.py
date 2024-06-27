import requests
from telebot import types
from utils import load_servers, save_servers, generate_unique_id
from config import SERVERS_FILE_TEMPLATE, DEFAULT_SERVER, MAX_SERVERS

def servers_handler(bot, message):
    chat_id = message.chat.id
    servers = load_servers(chat_id, SERVERS_FILE_TEMPLATE, DEFAULT_SERVER)
    text = "Выберите из списка сервер для проверки статуса:"
    keyboard = types.InlineKeyboardMarkup()

    for server_id, server_info in servers.items():
        button = types.InlineKeyboardButton(text=f"{server_info['name']} (ID: {server_id})", callback_data=f"status_{server_id}")
        keyboard.add(button)

    bot.reply_to(message, text=text, reply_markup=keyboard)

def status_callback(bot, call):
    chat_id = call.message.chat.id
    servers = load_servers(chat_id, SERVERS_FILE_TEMPLATE, DEFAULT_SERVER)
    server_id = call.data.split("_")[1]
    server_info = servers.get(server_id)

    if not server_info:
        bot.reply_to(call.message, text="Сервер не найден.")
        return

    server_address = server_info["address"]
    response = requests.get(f"https://api.mcstatus.io/v2/status/bedrock/{server_address}")
    data = response.json()

    text = (f"ID: {server_id}\n"
            f"Статус: {'🟢Онлайн🟢' if data.get('online', False) else '🔴Оффлайн🔴'}\n"
            f"💭Онлайн: {data.get('players', {}).get('online')}/{data.get('players', {}).get('max')}\n"
            f"🌐Айпи: <code>{data.get('host', '')}</code>\n"
            f"🌐Порт: <code>{data.get('port', '')}</code>\n"
            f"🌐Версия: {data.get('version', {}).get('name')}")

    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text, parse_mode="html")

def add_server_handler(bot, message):
    chat_id = message.chat.id
    servers = load_servers(chat_id, SERVERS_FILE_TEMPLATE, DEFAULT_SERVER)
    args = message.text.split(maxsplit=2)

    if len(args) != 3:
        bot.reply_to(message, text="Использование: /add_server <название> <айпи:порт>")
        return

    server_name, server_address = args[1], args[2]

    if ':' not in server_address or len(server_address.split(':')) != 2:
        bot.reply_to(message, text="Неправильный формат айпи:порт. Используйте <айпи>:<порт>")
        return

    if len(servers) >= MAX_SERVERS:
        bot.reply_to(message, text="Извините, память переполнилась. Поэтому мы временно ограничили создания серверов до действий Создателя бота")
        return

    server_id = generate_unique_id(servers.keys())

    servers[server_id] = {"name": server_name, "address": server_address}
    save_servers(chat_id, servers, SERVERS_FILE_TEMPLATE)
    bot.reply_to(message, text=f"Сервер '{server_name}' добавлен с ID: {server_id}")

def delete_server_handler(bot, message):
    chat_id = message.chat.id
    servers = load_servers(chat_id, SERVERS_FILE_TEMPLATE, DEFAULT_SERVER)
    args = message.text.split(maxsplit=1)

    if len(args) != 2:
        bot.reply_to(message, text="Использование: /delete_server <ID>")
        return

    server_id = args[1]
    if server_id == "1":
        bot.reply_to(message, text="Не удалось удалить сервер. Причина: Создатель отключил возможность удаления сервера по умолчанию")
        return

    if server_id in servers:
        del servers[server_id]
        save_servers(chat_id, servers, SERVERS_FILE_TEMPLATE)
        bot.reply_to(message, text=f"Сервер с ID: {server_id} удален.")
    else:
        bot.reply_to(message, text="Сервер с указанным ID не найден.")