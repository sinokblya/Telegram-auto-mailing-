from telethon import TelegramClient

# Учетные данные для доступа
api_id = '28806684'
api_hash = '1cd60a7b1eee1da722a53d3fe7b7c609'
phone_number = '+79966103804'

# Создаем клиент Telegram
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone=phone_number)
    
    # Открываем файл для записи
    with open("chat_ids.txt", "w", encoding="utf-8") as file:
        async for dialog in client.iter_dialogs():
            # Формируем строку с названием и ID
            line = f"Название: {dialog.name}, ID: {dialog.id}\n"
            
            # Записываем строку в файл
            file.write(line)
            # Также можно вывести в консоль, если нужно
            print(line)

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())
