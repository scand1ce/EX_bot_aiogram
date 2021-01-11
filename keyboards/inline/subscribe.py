from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton




chek_back = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Проверить подписки",
                                     callback_data="check_subs")
            ]

        ]
)
