from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import contact_button

from loader import dp, bot


@dp.message_handler(Command("callback"))
async def share_number(message: types.Message):
    await message.answer(f"Здравствуйте, {message.from_user.full_name}.\n"
                         f"Для того, чтобы наш менеджер вам перезвонил поделитесь своим номером телефона "
                         f"нажав на кнопку ниже!", reply_markup=contact_button.keyboard)


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def get_contact(message: types.Message):
    contact = message.contact
    await message.answer(f"Спасибо, {contact.full_name}.\n"
                         f"Ваш номер {contact.phone_number} был получен и передан менеджеру. Ожидайте",
                         reply_markup=ReplyKeyboardRemove())