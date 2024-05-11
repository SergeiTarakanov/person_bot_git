from aiogram import Dispatcher, Bot
from aiogram.dispatcher import storage, FSMContext
# import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Command

import logging
# from bot import logger

from tgbot.keyboards.menu import menu
# from tgbot.services.db_pg_SQL.pg_SQL import Database

bot = Bot(token="6288576941:AAFnfoLo4LR90wrTNePMt3dDnHsQ1aSM9Fo", parse_mode='HTML')
dp = Dispatcher(bot, storage=storage)
# db = Database()
logger = logging.getLogger(__name__)

async def bot_start(message: types.Message):
    await message.answer("Выберите действие", reply_markup=menu)
    logger.info("Star")

def register_start(dp: Dispatcher):
    dp.register_message_handler(bot_start, Command("start"))
