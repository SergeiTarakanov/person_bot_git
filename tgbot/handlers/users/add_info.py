
from aiogram import Dispatcher, Bot
from aiogram import types
from aiogram.dispatcher import storage, FSMContext
from aiogram.dispatcher.filters.builtin import Command, Text

from tgbot.services.db_pg_SQL.pg_SQL import Database

bot = Bot(token="6288576941:AAFnfoLo4LR90wrTNePMt3dDnHsQ1aSM9Fo", parse_mode='HTML')
dp = Dispatcher(bot, storage=storage)


db = Database()

async def bot_add(message: types.Message, state: FSMContext):
    await message.answer("Пришлите информацию которую хотите добавить БД")
    await state.set_state("add")

async def enter_add(message: types.Message, state: FSMContext):
    await db.create_table_info()
    info = message.text
    await db.add_info(full_info=info)
    # users = db.select_all_users()
    # await message.answer(f"Данные обновлены. Запись в БД: {users}")
    # print(f"Получил всех пользователей: {users}")
    await state.finish()
    x = await db.select_all_info()
    print(f"БД: {x}")
    count = await db.count_info()
    num = count-1
    await message.answer(f"Вы дабавили: {x[num][1]}")

async def del_tabl(message: types.Message):
    await db.drop_info()

def register_add_db(dp: Dispatcher):
    # dp.register_message_handler(bot_add, Command("add"))
    dp.register_message_handler(bot_add, Text(equals=["добавить заметку", "Пюрешка"]))
    dp.register_message_handler(del_tabl, Text(equals=["удалить данные"]))
    dp.register_message_handler(enter_add, state="add")
