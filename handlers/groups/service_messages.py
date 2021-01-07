from aiogram.types import ContentType, Message

from filters import IsGroup
from loader import dp, bot


@dp.message_handler(IsGroup(), commands=ContentType.LEFT_CHAT_MEMBER)
async def banned_member(message: Message):
    print('22222222')
    if message.left_chat_member.id == message.from_user.id:
        await message.answer(f"{message.left_chat_member.get_mention(as_html=True)} вышел из чата.")
    elif message.from_user.id == (await bot.me).id:
        return
    else:
        await message.reply(f"{message.left_chat_member.full_name} был удален из чата "
                            f"пользователем {message.from_user.get_mention(as_html=True)}.")


@dp.message_handler(IsGroup(), content_types=ContentType.NEW_CHAT_MEMBERS)
async def new_member(message: Message):
    print('11111111')
    members = ", ".join([m.get_mention(as_html=True) for m in message.new_chat_members])
    await message.reply(f"Привет, {members}!")
