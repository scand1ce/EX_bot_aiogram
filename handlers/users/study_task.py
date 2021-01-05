import logging

import emoji
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import buy_callback
from keyboards.inline.study_task_buttons import buttons
from loader import dp, bot


@dp.message_handler(Command('item'))
async def item(message: types.Message):
    await bot.send_photo(
                        chat_id=message.from_user.id,
                        photo="https://d05c960b-0698-4405-ba5e-353903867a1b.selcdn.net/image/cache/data/"
                              "tovary/handgun-wolf-01/Ugears-Handgun-Mechanical-Model-1--Title-530x380.jpg",
                        caption=f'Пистолет {emoji.emojize(":thumbs_up:")}',
                        reply_markup=buttons
                    )


@dp.callback_query_handler(buy_callback.filter(item_name="Покупай товар № "))
async def buying_phone(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f'callback_data = {call.data}')
    logging.info(f'callback_data dict = {callback_data}')
    gun = callback_data.get('item_name')
    one = callback_data.get('quantity')
    await call.bot.send_photo(
                        chat_id=call.from_user.id,
                        photo="https://d05c960b-0698-4405-ba5e-353903867a1b.selcdn.net/image/cache/data/"
                              "tovary/handgun-wolf-01/Ugears-Handgun-Mechanical-Model-1--Title-530x380.jpg",
                        caption=f'{gun}{one}',
                        reply_markup=buttons
                    )

@dp.callback_query_handler(text="Вам понравился этот товар")
async def like(call: CallbackQuery):
    # Ответим в окошке с уведомлением!
    await call.answer("Вам понравился этот товар")


@dp.callback_query_handler(text="Вам не понравился этот товар")
async def dislike(call: CallbackQuery):
    # Ответим в окошке с уведомлением!
    await call.answer("Вам не понравился этот товар")
