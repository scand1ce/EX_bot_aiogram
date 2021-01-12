from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("test", "Тестирование"),
        types.BotCommand("form", "Запрос данных пользователя"),
        types.BotCommand("menu", "Меню с кнопками"),
        types.BotCommand("items", "Инлайн кнопки"),
        types.BotCommand("item", "Задание с инлайн кнопками"),
        types.BotCommand("format", "Варианты форматирования текста"),
        types.BotCommand("set_photo", "Установить фото в чате"),
        types.BotCommand("set_title", "Установить название группы"),
        types.BotCommand("set_description", "Установить описание группы"),
        types.BotCommand("ro", "Режим Read Only"),
        types.BotCommand("unro", "Отключить RO"),
        types.BotCommand("ban", "Забанить"),
        types.BotCommand("unban", "Розбанить"),
        types.BotCommand("channels", "Список каналов"),
        types.BotCommand("create_post", "Предложить пост в канале"),
        types.BotCommand("help", "Помощь")

    ])