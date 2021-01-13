from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.location_buttons import keyboard
from loader import dp
from utils.misc.calc_distance import choose_shortest


@dp.message_handler(Command("show_on_map"))
async def share_number(message: types.Message):
    await message.answer(f"Здравствуйте, {message.from_user.full_name}.\n"
                         f"Для того, чтобы показать ближайшие магазины отправьте нам свою локацию "
                         f"нажав на кнопку ниже!", reply_markup=keyboard)


@dp.message_handler(content_types=types.ContentType.LOCATION)
async def get_contact(message: types.Message):
    location = message.location
    latitude = location.latitude
    longitude = location.longitude
    closest_shops = choose_shortest(location)

    text = "\n\n".join([f"Название: {shop_name}. <a href='{url}'>Google</a>\n Расстояние до него: {distance:.1f} км."
                        for shop_name, distance, url, shop_location in closest_shops])

    await message.answer(f"Спасибо. \n"
                         f"Latitude = {latitude}\n"
                         f"Longitude = {longitude}\n\n"
                         f"{text}", disable_web_page_preview=True, reply_markup=ReplyKeyboardRemove())

    for shop_name, distance, url, shop_location in closest_shops:
        await message.answer_location(latitude=shop_location["lat"],
                                      longitude=shop_location["lon"])
