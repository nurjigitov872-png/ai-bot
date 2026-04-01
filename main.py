import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = "8665777185:AAE5bOhhe0NtWuTL-Vtad3mOI1xYAsoXFUs"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# /start
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "👋 Салам!\nМен AI Бизнес ботмун 🤖\n\nКомандалар:\n/help - жардам\n/ai - суроо жаз"
    )

# help
@dp.message(Command("help"))
async def help_cmd(message: types.Message):
    await message.answer(
        "📌 Колдонуу:\n\n/ai текст жаз → мен жооп берем"
    )

# AI чат (жөнөкөй версия)
@dp.message(Command("ai"))
async def ai_chat(message: types.Message):
    text = message.text.replace("/ai", "").strip()

    if not text:
        await message.answer("❗ Суроо жаз: /ai сенин сурооң")
        return

    # азырынча жөнөкөй жооп (OpenAI кийин кошобуз)
    await message.answer(f"🤖 Сен жаздың: {text}\n\n(бул AI логикага туташат)")

# run bot
async def main():
    print("Bot иштеп жатат...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())