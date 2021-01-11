from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from filters.forwarded_message import IsForwaeded
from loader import dp
from keyboards.inline.subscribe import chek_back
from utils.misc import subscribe


@dp.message_handler(IsForwaeded(), content_types=types.ContentType.ANY)
async def get_channel_info(message: types.Message):
    await message.answer(f"{message.forward_from_chat.title}\n"
                         f"Username: @{message.forward_from_chat.username}\n"
                         f"ID: {message.forward_from_chat.id}")

@dp.message_handler(Command("channels"))
async def show_channels(message: types.Message):
    channels_format = str()
    # chat = [await bot.get_chat(channel_id_or_username) for channel_id_or_username in channels]
    for channel_id_or_username in channels:
        chat = await bot.get_chat(channel_id_or_username)
        invite_link = await chat.export_invite_link()
        channels_format += f"Канал <a href='{invite_link}'>{chat.title}</a>\n\n"
    await message.answer(
                         f"Каналы:\n{channels_format}",
                         reply_markup=chek_back,
                         disable_web_page_preview=True
                         )

@dp.callback_query_handler(text="check_subs")
async def checker(call: CallbackQuery):
    await call.answer()
    result = str()
    for channel in channels:
        status = await subscribe.check(user_id=call.from_user.id, channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            result += f"Подписка на канал <b>{channel.title}</b> Оформлена!\n\n"
        else:
            invite_kink = await channel.export_ivite_link()
            result += f"Подписка на канал <b>{channel.title}</b> не оформлена!\n" \
                      f"<a href='{invite_kink}'>Нужно подписаться!</a> \n\n"
    await call.message.answer(result, disable_web_page_preview=False)