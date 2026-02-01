import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlres import BotHandlers 

async def main():
   
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

   
    handlers = BotHandlers(bot)
    dp.include_router(handlers.router)

    print("Бот успешно запущен! Напиши ему в Telegram.")
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Бот остановлен")