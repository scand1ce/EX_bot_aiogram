from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import emoji
from keyboards.inline.callback_datas import buy_callback
from loader import bot


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
    ],
)

switch_button = InlineKeyboardButton(text="Поделиться с другом", switch_inline_query="")
buttons.add(switch_button)
