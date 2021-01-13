from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile

from loader import dp, bot


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_file_id_p(message: types.Message):
    await message.reply(message.photo[-1].file_id)


@dp.message_handler(content_types=types.ContentType.VIDEO)
async def get_file_id_v(message: types.Message):
    await message.reply(message.video.file_id)


@dp.message_handler(Command("get_cat"))
async def send_cat(message: types.Message):
    # photos = "AgACAgIAAxkBAAICcV6jF5kAARvDMn99PQuVe9fBg-TKcAACQ64xG0WQGEm4F3v9dsbAAg7Hwg8ABAEAAwIAA3kAA9c_BgABGQQ"  #
    # File id
    photo = "https://www.meme-arsenal.com/memes/3f5777727d3f6e263b4edbee5bd15a1b.jpg" # URL
    # photos = InputFile(path_or_bytesio="photos/cat.jpg")  # Local file
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=photo,
                         caption="Вот тебе фото кота /more_cats")


@dp.message_handler(Command("more_cats"))
async def more_cats(message: types.Message):
    # Создаем альбом
    album = types.MediaGroup()

    # Прикрепляем фото и видео
    photo_file_id = "AgACAgQAAxkBAAIVM1_-yU7mgUyETs3gagU_IHFQh-xnAAI1qjEbDx49UYQ0V4VxJ8L9BEWoGwAEAQADAgADdwAD5EMDAAEeBA"
    photo_url = "https://i.pinimg.com/originals/13/25/68/132568dbe8f3316aa56551dba527e7f7.jpg"
    photo_bytes = InputFile("photos/cat.jpg")
    video_file_id = "BAACAgIAAxkBAAIVWV_-zXn0882_0595Trr0Ow_k1nLsAALhCQACDznpSYEyFf09bJB2HgQ"
    album.attach_photo(
        photo=photo_file_id,
        caption="Прикольный котик")
    album.attach_photo(photo=photo_url)
    album.attach_photo(photo=photo_bytes)
    album.attach_video(video=video_file_id,
                       caption="Видео")

    # Отправляем
    # await bot.send_media_group(chat_id=message.from_user.id, media=album)
    await message.answer_media_group(media=album)
