
import asyncio
import datetime
import re

import aiogram
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.utils.exceptions import BadRequest

from filters import IsGroup, AdminFilter
from loader import dp, bot


# Хендлер с фильтром в группе, где можно использовать команду !ro ИЛИ /ro
@dp.message_handler(IsGroup(), Command("ro", prefixes="!/"), AdminFilter())
async def read_only_mode(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id
    command_parse = re.compile(r"(!ro|/ro) ?(\d+)? ?([\w+\D]+)?")
    parsed = command_parse.match(message.text)
    time = parsed.group(2)
    comment = parsed.group(3)
    if not time:
        time = 5

    """
    !ro 
    !ro 5 
    !ro 5 test
    !ro test
    !ro test test test
    /ro 
    /ro 5 
    /ro 5 test
    /ro test
    """
    # Пример 1
    # !ro 5
    # command='!ro' time='5' comment=[]

    # Пример 2
    # !ro 50 читай мануал
    # command='!ro' time='50' comment=['читай', 'мануал']

    time = int(time)

    # Получаем конечную дату, до которой нужно забанить
    until_date = datetime.datetime.now() + datetime.timedelta(minutes=time)

    # Вариант 1 - по API
    # await bot.restrict_chat_member(chat_id=chat, user_id=member,  can_send_messages=False, until_date=until_date)

    # Вариант 2 - сокращенный
    try:
        await message.chat.restrict(user_id=member_id, can_send_messages=False, until_date=until_date)
        await message.reply_to_message.delete()
    except aiogram.utils.exceptions.BadRequest as err:
        await message.answer(f"Ошибка! {err.args}")
        return

    # Пишем в чат
    await message.answer(f"Пользователю {message.reply_to_message.from_user.full_name} запрещено писать {time} минут.\n"
                         f"По причине: \n<b>{comment}</b>")

    service_message = await message.reply("Сообщение самоуничтожится через 5 секунд.")
    # Пауза 5 сек
    await asyncio.sleep(5)

    # Удаляем сообщения
    # Вариант 1 - по API
    # await bot.delete_message(chat_id=chat_id, message_id=message.message_id)

    # Вариант 2 - сокращенный
    await message.delete()
    await service_message.delete()


@dp.message_handler(IsGroup(), Command("ban", prefixes="!/"), AdminFilter())
async def ban_user(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id

    # Вариант 1 - по API
    # await bot.kick_chat_member(chat_id=chat_id, user_id=member)

    # Вариант 2 - сокращенный
    await message.chat.kick(user_id=member_id)

    # Пишем в чат
    await message.answer(f"Пользователь {message.reply_to_message.from_user.full_name} был забанен")
    service_message = await message.reply("Сообщение самоуничтожится через 5 секунд.")

    # Пауза 5 сек
    await asyncio.sleep(5)

    # Удаляем сообщения
    await message.delete()
    await service_message.delete()


@dp.message_handler(IsGroup(), Command("unban", prefixes="!/"), AdminFilter())
async def unban_user(message: types.Message):
    member = message.reply_to_message.from_user
    member_id = member.id
    chat_id = message.chat.id
    await message.chat.unban(user_id=member_id)
    # Пишем в чат
    await message.answer(f"Пользователь {message.reply_to_message.from_user.full_name} был разбанен")
    service_message = await message.reply("Сообщение самоуничтожится через 5 секунд.")

    # Пауза 5 сек
    await asyncio.sleep(5)

    # Удаляем сообщения
    await message.delete()
    await service_message.delete()