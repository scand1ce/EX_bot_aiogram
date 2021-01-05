from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inline.callback_datas import buy_callback

choice = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                        text="Купить телефон",
                        callback_data=buy_callback.new(item_name='phone',
                                                       quantity=1)
                ),
                InlineKeyboardButton(
                        text="Купить ноутбук",
                        callback_data="buy:notebook:7"
                )
            ],
            [
                InlineKeyboardButton(
                        text="ОТМЕНА",
                        callback_data="cancel"
                )
            ]
        ]
)


note_keyboard = InlineKeyboardMarkup()

NOTE_LINK = "https://www.google.com/search?q=notebooks"

note_link = InlineKeyboardButton(text="Ноутбуки можно посмотреть здесь!", url=NOTE_LINK)

note_keyboard.insert(note_link)
