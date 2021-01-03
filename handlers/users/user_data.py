from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states import UserForm


@dp.message_handler(Command('form'))
async def get_user_data(message: types.Message):
    await message.answer("Введите <b>имя</b> и\nотправьте его боту!")
    await UserForm.first()


@dp.message_handler(state=UserForm.name)
async def get_email(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(
            {
                "name": name
            }
    )
    await message.answer("Введите <b>адрес электронной почты</b>\n"
                         "и отправьте его буту!")
    await UserForm.next()


@dp.message_handler(state=UserForm.email)
async def get_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(
            {
                "email": email
            }
    )
    await message.answer("Введите <b>номер телефона</b>\n"
                         "и отправьте его боту!")
    await UserForm.next()


@dp.message_handler(state=UserForm.phone)
async def get_phone(message: types.Message, state: FSMContext):
    data = await state.get_data()
    name = data.get('name')
    email = data.get('email')
    phone = message.text

    await message.answer(
            "Привет!\n"
            "Ты ввел следующие данные:\n"
            f"Имя - <b>{name}</b>\n"
            f"Email - <b>{email}</b>\n"
            f"Телефон: - <b>{phone}</b>")
    await state.reset_state(with_data=True)