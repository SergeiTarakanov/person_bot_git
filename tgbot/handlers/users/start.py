from aiogram import Dispatcher, Bot
from aiogram.dispatcher import storage, FSMContext
# import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Command

from tgbot.keyboards.menu import menu
from tgbot.services.db_pg_SQL.pg_SQL import Database

bot = Bot(token="6288576941:AAFnfoLo4LR90wrTNePMt3dDnHsQ1aSM9Fo", parse_mode='HTML')
dp = Dispatcher(bot, storage=storage)
db = Database()


async def bot_start(message: types.Message):
    await message.answer("Выберите товар из меню ниже", reply_markup=menu)

# async def bot_start2(message: types.Message):
#     await db.create_table_info()
#     await message.answer("начинаем работу")
#     text='Второй совет'
#     await db.add_info(full_info=text)
#     # await db.add_info()
#     x = await db.select_all_info()
#     print(f"Получил всех пользователей: {x}")
#
#     await message.answer(f"Получил 1 пользователя: {x[0][1]}")

def register_start(dp: Dispatcher):
    dp.register_message_handler(bot_start, Command("start"))
