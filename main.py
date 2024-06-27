import time
from telebot import TeleBot, types
from config import TOKEN
from handlers import start_handler, about_handler, upgrade_handler, botping_handler, is_private_chat
from server_handlers import servers_handler, status_callback, add_server_handler, delete_server_handler

bot = TeleBot(TOKEN)

@bot.message_handler(func=is_private_chat, commands=['start'])
def handle_start(message):
    start_handler(bot, message)

@bot.message_handler(func=is_private_chat, commands=['about'])
def handle_about(message):
    about_handler(bot, message)

@bot.message_handler(func=is_private_chat, commands=['upgrade'])
def handle_upgrade(message):
    upgrade_handler(bot, message)

@bot.message_handler(func=is_private_chat, commands=['botping'])
def handle_botping(message):
    botping_handler(bot, message)

@bot.message_handler(func=is_private_chat, commands=['servers'])
def handle_servers(message):
    servers_handler(bot, message)

@bot.callback_query_handler(func=lambda call: call.data.startswith("status_"))
def handle_status_callback(call):
    status_callback(bot, call)

@bot.message_handler(func=is_private_chat, commands=['add_server'])
def handle_add_server(message):
    add_server_handler(bot, message)

@bot.message_handler(func=is_private_chat, commands=['delete_server'])
def handle_delete_server(message):
    delete_server_handler(bot, message)

def main():
    print(f"========\nБот запущен\nЗдравствуй, Фикс!\n========")
    bot.infinity_polling()

if __name__ == "__main__":
    main()