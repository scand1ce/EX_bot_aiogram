import io
import logging

from aiogram import types
from aiogram.dispatcher.filters import AdminFilter, Command

from filters import IsGroup
from loader import dp


@dp.message_handler(IsGroup(), AdminFilter(), Command("set_photo"))
async def set_new_photo(message: types.Message):
    source_message = message.reply_to_message
    photo = source_message.photo[-1]
    photo = await photo.download(destination=io.BytesIO())
    input_file = types.InputFile(photo)

    try:
        await message.chat.set_photo(photo=input_file)
        await message.reply("Фото было успешно обновлено.")
    except Exception as err:
        logging.exception(err)


@dp.message_handler(IsGroup(), AdminFilter(), Command("set_title"))
async def set_new_title(message: types.Message):
    source_message = message.reply_to_message
    title = source_message.text
    # Вариант 1
    # await bot.set_chat_title(message.chat.id, title=title)

    # Вариант 2
    await message.chat.set_title(title=title)


@dp.message_handler(IsGroup(), AdminFilter(), Command("set_description"))
async def set_new_description(message: types.Message):
    source_message = message.reply_to_message
    description = source_message.text

    # Вариант 1
    # await bot.set_chat_description(message.chat.id, description=description)

    # Вариант 2
    await message.chat.set_description(description=description)