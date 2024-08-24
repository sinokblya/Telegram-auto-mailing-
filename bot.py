from telethon import TelegramClient, events, Button
import asyncio

# Вставьте свои данные ниже
api_id = '28806684'
api_hash = '1cd60a7b1eee1da722a53d3fe7b7c609'
bot_token = '6485589346:AAGSB1T35P9P1WAsRMTJAAmX8CtDNntaKx4'

# Создание клиента
client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    # Первое сообщение с кнопкой
    await event.respond(
        "Стань курьером прямо сейчас https://clck.ru/3Cbonr",
        buttons=[Button.url("Стать курьером!", "https://clck.ru/3Cbonr")]
    )
    
    # Ожидание 5 минут
    await asyncio.sleep(300)
    
    # Второе сообщение с кнопкой
    await event.respond(
        "Также предлагаем оформить Альфа-карту с повышенным кэшбеком и получить дополнительные 500 рублей. Также можешь использовать эту карту как расчетный счет для получения выплат с доставок https://alfa.me/WeLsyo",
        buttons=[Button.url("Оформить карту!", "https://alfa.me/WeLsyo")]
    )

# Запуск бота
client.run_until_disconnected()
