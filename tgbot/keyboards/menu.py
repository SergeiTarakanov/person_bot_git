
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="добавить заметку"),
        ],
        [
            KeyboardButton(text="Посмотреть заметку"),
            KeyboardButton(text="удалить данные")
        ],
    ],
    resize_keyboard=True
)