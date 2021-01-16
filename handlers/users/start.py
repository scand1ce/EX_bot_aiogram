from re import compile

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from filters import IsPrivate
from loader import dp, db
from utils.misc import rate_limit
from utils.db_api.user import User

import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        print(err)
    count = db.count_users()[0]
    await message.answer(
        "\n".join(
            [
                f'Привет, {message.from_user.full_name}!',
                f'Ты был занесен в базу',
                f'В базе <b>{count}</b> пользователей',
            ]))
"""# Этот хендлер используется для диплинков в личной переписке:
# Когда пользователь переходит по ссылке http://t.me/username_bot?start=123
# Тогда по нажатию на кнопку start - боту приходит команда старт с аргументом 123
# Тогда мы можем отловить этот диплинк с помощью регулярных выражений (функция compile)
# \d\d\d - значит, что мы ловим 3 цифры подряд. (\d) - одна цифра
@rate_limit(limit=5)
# @dp.message_handler(CommandStart(deep_link=compile(r"\d\d\d")), IsPrivate())
@dp.message_handler(CommandStart())
# async def bot_start_deeplink(message: types.Message, user: User):
async def bot_start(message: types.Message):
    # С помощью функции get_args забираем аргументы после команды start. (для примера выше - будет "123")
    deep_link_args = message.get_args()

    await message.answer(f'Привет, {message.from_user.full_name}!\n'
                         f'Вы находитесь в личной переписке. \n'
                         f'В вашей команде есть диплинк\n'
                         f'Вы передали аргумент {deep_link_args}.\n')
                         # f'Юзер полученный через миддлварь: {user.__dict__}')"""


"""# В этом хендлере мы ловим простое нажатие на команду /start, не прошедшее под условие выше
@dp.message_handler(CommandStart(deep_link=None), IsPrivate())
# async def bot_start(message: types.Message, user: User):
async def bot_start(message: types.Message):
    # Для создания диплинк-ссылки - нужно получить юзернейм бота
    bot_user = await dp.bot.get_me()

    # Формируем диплинк-ссылку
    deep_link = f"http://t.me/{bot_user.username}?start=123"
    await message.answer(f'Привет, {message.from_user.full_name}!\n'
                         f'Вы находитесь в личной переписке. \n'
                         f'В вашей команде нет диплинка.\n'
                         f'Ваша диплинк ссылка - {deep_link}\n')
                         # f'Юзер полученный через миддлварь: {user.__dict__}')"""
