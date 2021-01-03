from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("test", "Тестирование"),
        types.BotCommand("form", "Запрос данных пользователя"),
        types.BotCommand("menu", "Меню с кнопками"),
        types.BotCommand("help", "Помощь")

    ])