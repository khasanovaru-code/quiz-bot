# Файл config.py
BOT_TOKEN = "8421009902:AAFnWyYgXG9ykZQvpF0eioInnBIL9BRpgak"
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}! Твой бот теперь работает!")



async def main():
    print("Бот запущен и готов к работе...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")