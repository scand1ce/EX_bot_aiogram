from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from utils.misc import rate_limit


# Используем тут фильтр на команду /help. rate_limit - миддлварь, который не дает флудить этой командой
# (выполнение раз в 5 секунд)
@rate_limit(5, 'help')
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    # Формируем ответ пользователю с помощью строк, которые мы потом соединим символом "\n" - новая строка
    text = [
        'Список команд: ',
        '/start - Начать',
        '/test - Тестирование',
        '/form - Форма для пользователя',
        '/menu - Меню',
        '/items - Инлайн кнопки',
        '/item - Задание с инлайн кнопками',
        '/format - Варианты форматирования текста',
        '/set_pthoto - Установить фото в чате',
        '/set_title - Установить название группы',
        '/set_description - Установить описание группы',
        '/ro - Режим Read Only',
        '/unro - Отключить RO',
        '/ban - Забанить',
        '/unban" - "Розбанить',
        '/channels - Список каналов',
        '/create_post - Предложить пост в канале',
        '/help - Справка'
    ]
    await message.answer('\n'.join(text))
