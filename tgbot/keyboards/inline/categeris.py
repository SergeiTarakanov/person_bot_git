from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

category_callback = CallbackData("category", "categ")

category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="сератонин", callback_data=category_callback.new(categ="сератонин")),
        InlineKeyboardButton(text="окстацин", callback_data="category:окстацин"),
        InlineKeyboardButton(text="дофамин", callback_data="category:дофамин"),
        InlineKeyboardButton(text="кортизол", callback_data="category:кортизол"),
    ]]
)
# Вариант 1, как в прошлом уроке
# choice = InlineKeyboardMarkup(inline_keyboard=[
#     [
#         InlineKeyboardButton(text="Купить грушу", callback_data=buy_callback.new(item_name="pear")),
#         InlineKeyboardButton(text="Купить яблоки", callback_data="buy:apple")
#     ],
#     [
#         InlineKeyboardButton(text="Отмена", callback_data="next")
#     ]
# ])




# category_keyboard = InlineKeyboardMarkup(
#     inline_keyboard=[[
#         InlineKeyboardButton(text="сератонин", callback_data="seratonin")
#     ]]
# )

# check_button = InlineKeyboardMarkup(
#     inline_keyboard=[[
#         InlineKeyboardButton(text="Проверить подписки", callback_data="check_subs")
#     ]]
# )