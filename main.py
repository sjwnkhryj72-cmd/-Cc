import os
import random
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv
import data

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# لوحة الأوامر
def get_main_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton("💎 زخرفة اسم"), KeyboardButton("📝 زخرفة بايو"))
    kb.add(KeyboardButton("🎂 زخرفة مواليد"), KeyboardButton("✨ أسماء جاهزة"))
    return kb

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("أهلاً بك يا دراكون، اختر خدمتك:", reply_markup=get_main_menu())

@dp.message_handler(text="📝 زخرفة بايو")
async def send_bio(message: types.Message):
    await message.answer(random.choice(data.bio_quotes_ar))

@dp.message_handler(text="✨ أسماء جاهزة")
async def send_ready_names(message: types.Message):
    ar = random.sample(data.arabic_names, min(len(data.arabic_names), 2))
    en = random.sample(data.english_names, min(len(data.english_names), 2))
    await message.answer(f"أسماء عربية: {', '.join(ar)}\n\nأسماء إنجليزية: {', '.join(en)}")

@dp.message_handler(text="💎 زخرفة اسم")
async def ask_name(message: types.Message):
    await message.answer("أرسل الاسم الذي تريد زخرفته:")

@dp.message_handler()
async def decorate_name(message: types.Message):
    # هنا الزخرفة المتغيرة العشوائية
    style = random.choice(list(data.decor_styles.values()))
    await message.answer(f"النتيجة:\n\n{style.format(message.text)}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

