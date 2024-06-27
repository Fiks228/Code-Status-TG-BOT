import time

def is_private_chat(message):
    return message.chat.type == 'private'

def start_handler(bot, message):
    text = (
        "Привет! Это Статус бот проекта 'CoolAnarchy'. Мы всегда рады другим игрокам. "
        "Ссылка на нашу группу @CooIAnarchy\nСписок команд:\n"
        "/servers - Показывает статус серверов\n"
        "/add_server <название> <айпи:порт> - Добавляет новый сервер\n"
        "/delete_server <ID> - Удаляет сервер по ID\n"
        "/about - Инфа\n/upgrade - Обновления бота\n/botping - Пинг Бота"
    )
    bot.reply_to(message, text=text)

def about_handler(bot, message):
    text = (
        "📳Наш тг: @CooIAnarchy\n📳Наш тик ток: https://www.tiktok.com/@CoolAnarchy\n"
        "📳Наш бусти: https://boosty.to/shopruda\n📳Создал и накодил бота fiks_official"
    )
    bot.reply_to(message, text=text)

def upgrade_handler(bot, message):
    text = (
        "Обновления бота и сервера:\n"
        "1️⃣ Фриз спит [troll face:)]\n"
        "2️⃣ Никто не звиздит\n"
        "3️⃣ В текст добавил смайлики\n"
        "4️⃣ Добавил ссылку на сервер!!!\n"
        "5️⃣ Добавил /botping"
    )
    bot.reply_to(message, text=text)

def botping_handler(bot, message):
    start_time = time.time()
    bot.reply_to(message, text="Измеряю пинг бота...")
    ping_time = round((time.time() - start_time) * 1000, 2)
    text = f"Пинг бота: {ping_time} мс"
    bot.reply_to(message, text=text)