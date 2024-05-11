
from aiogram import Dispatcher, Bot
from aiogram import types
from aiogram.dispatcher import storage, FSMContext
from aiogram.dispatcher.filters.builtin import Command, Text
from aiogram.types import CallbackQuery, callback_query, ReplyKeyboardRemove
from aiogram.utils import callback_data
import logging

from tgbot.keyboards.inline.categeris import category_keyboard, category_callback
from tgbot.services.db_pg_SQL.pg_SQL import Database

bot = Bot(token="6288576941:AAFnfoLo4LR90wrTNePMt3dDnHsQ1aSM9Fo", parse_mode='HTML')
dp = Dispatcher(bot, storage=storage)
logger = logging.getLogger(__name__)

db = Database()

async def bot_add(message: types.Message, state: FSMContext):
    await message.answer("Пришлите информацию которую хотите добавить БД", reply_markup=ReplyKeyboardRemove())
    await state.set_state("add")
    logger.info("bot_add")

async def enter_add(message: types.Message, state: FSMContext):
    logger.info("enter_add 1")
    await db.create_table_info()
    logger.info("enter_add 2")
    # global info
    # info = message.text
    await message.answer(f"в каую категорию добавить?",
                         reply_markup=category_keyboard)

    await state.set_state("add2")

async def confirm_post(call: CallbackQuery, callback_data:dict, state: FSMContext):
    print(f"заходим в CallbackQuery! ")
    info ='пока обычный текст'
    # убираем часики с инлайн кнопки
    await call.answer()
    info2 = callback_data.get("categ")
    print(f"ПЕЧАТАЮ ИНФОРМАЦИЮ! info2 {info2}")
    print(f"ПЕЧАТАЮ ИНФОРМАЦИЮ info! {info}")

    await db.add_info(full_info=info, category=info2)
    await state.finish()
    # удаляем клавиатуру инлайн
    await call.message.edit_reply_markup()
    x = await db.select_all_info()
    print(f"БД: {x}")
    count = await db.count_info()
    num = count-1
    await call.message.answer(f"Вы дабавили: {x[num][1]}")
async def del_tabl(message: types.Message):
    await db.drop_info()
    await message.answer(f"данные удалены")

def register_add_db(dp: Dispatcher):
    # dp.register_message_handler(bot_add, Command("add"))
    dp.register_message_handler(bot_add, Text(equals=["добавить заметку", "Пюрешка"]))
    dp.register_message_handler(del_tabl, Text(equals=["удалить данные"]))
    dp.register_message_handler(enter_add, state="add")
    dp.register_callback_query_handler(confirm_post, category_callback.filter(categ=["сератонин", "окстацин", "дофамин", "кортизол"]), state="add2")


