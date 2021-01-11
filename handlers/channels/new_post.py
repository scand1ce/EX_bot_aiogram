import logging

from aiogram import types

from loader import dp, bot


@dp.channel_post_handler(content_types=types.ContentType.ANY)
async def new_post(message: types.Message):
    logging.info(f"Опубликовано новове сообщение в канале {message.chat.title}.\n"
                 f"{message.text}")


    await message.forward(chat_id='@ec_group')