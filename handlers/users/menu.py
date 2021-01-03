from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import menu
from loader import dp


@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
    await message.answer("Выберите товар в меню ниже", reply_markup=menu)


@dp.message_handler(text='Кнопка1')
async def get_cotletki(message: types.Message):
    await message.answer("Вы выбрали Кнопка1!")


@dp.message_handler(Text(equals=['Кнопка2', 'Кнопка3']))
async def get_cotletki(message: types.Message):
    await message.answer(f"Вы выбрали {message.text}!", reply_markup=ReplyKeyboardRemove())
