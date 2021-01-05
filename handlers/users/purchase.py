import logging

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import buy_callback
from keyboards.inline.choise_buttons import choice, note_keyboard
from loader import dp


@dp.message_handler(Command('items'))
async def show_items(message: types.Message):
    await message.answer(text="На продажу у нас есть 2 товара:\n"
                              "<b>1) 5 телефонов</b>\n"
                              "<b>2) 7 ноутбуков</b>\n"
                              "Если Вам ничего не нужно нажмите <b>ОТМЕНА</b>",
                         reply_markup=choice
                         )

@dp.callback_query_handler(buy_callback.filter(item_name="phone"))
async def buying_phone(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f'callback_data = {call.data}')
    logging.info(f'callback_data dict = {callback_data}')
    quantity = callback_data.get('quantity')
    await call.message.answer(f'You buying {quantity} phones',
                              reply_markup=note_keyboard)

@dp.callback_query_handler(buy_callback.filter(item_name="notebook"))
async def buying_apples(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)

    # Выведем callback_data и тут, чтобы сравнить с предыдущим вариантом.
    logging.info(f"{callback_data=}")

    quantity = callback_data.get("quantity")
    await call.message.answer(f"Вы выбрали купить notebook. Notebooks всего {quantity}. Спасибо.")


@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
    # Ответим в окошке с уведомлением!
    await call.answer("Вы отменили эту покупку!", show_alert=True)

    # Вариант 1 - Отправляем пустую клваиатуру изменяя сообщение, для того, чтобы ее убрать из сообщения!
    await call.message.edit_reply_markup(reply_markup=None)
