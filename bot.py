import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message

BOT_TOKEN = "8851040047:AAFUjwyCMSErmpTSWElBLOgZELHTaBTrmdU"

PASSWORD = "000067"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer("Введи шестизначное число:")

@dp.message()
async def guess_number_handler(message: Message):
    if message.text == PASSWORD:
        await message.answer("Да")
    else:
        await message.answer("Нет")

async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
