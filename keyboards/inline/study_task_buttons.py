from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import emoji
from keyboards.inline.callback_datas import buy_callback


buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                        text="Купить товар",
                        callback_data="buy:Покупай товар № :1"
                )
            ],

            [
                InlineKeyboardButton(
                        text=emoji.emojize(":thumbs_up:"),
                        callback_data='Вам понравился этот товар'

                ),
                InlineKeyboardButton(
                        text=emoji.emojize(":thumbs_down:"),
                        callback_data='Вам не понравился этот товар'

                ),
            ],
            [
                InlineKeyboardButton(
                        text="Поделиться с другом",
                        url="https://www.google.com/search?q="

                ),
            ]

        ],
)
