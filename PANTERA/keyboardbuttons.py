from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

button=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Fikir bildiring"),
            KeyboardButton(text="ulashish",request_contact=True)

        ]

    ],
    resize_keyboard=True
)