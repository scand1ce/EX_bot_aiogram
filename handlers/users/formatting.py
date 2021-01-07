from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.utils.markdown import hbold, hcode, hitalic, hunderline, hstrikethrough, hpre
from loader import dp


@dp.message_handler(Command('format'))
async def variants_formatting(message: types.Message):
    await message.answer(hbold('hbold'))
    await message.answer(hcode('hcode'))
    await message.answer(hitalic('hitalic'))
    await message.answer(hunderline('hunderline'))
    await message.answer(hstrikethrough('hstrikethrough'))
    await message.answer(hpre('hpre'))
