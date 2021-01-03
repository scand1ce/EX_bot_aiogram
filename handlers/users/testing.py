from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states import Test


@dp.message_handler(Command("test"))
async def enter_test(message: types.Message):
    await message.answer("Вы начали тестирование.\n"
                         "Вопрос №1\n\n"
                         "1?1?1?"
                         "фывафывафывафыавфыва")

    # await Test.Q1.set()
    await Test.first()


@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text

    # await state.update_data(anser1=answer)
    await state.update_data(
            {
                "answer1": answer
            }
    )

    # async with state.proxy() as data:
    #     data['answer1'] = answer

    await message.answer("Вопрос №2\n\n"
                         "22?22??")

    # await Test.Q2.set()
    await Test.next()


@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get('answer1')
    answer2 = message.text

    await message.answer("Спасибо за ответы!")
    await message.answer(f"answer1: {answer1}")
    await message.answer(f"answer2: {answer2}")

    await state.reset_state(with_data=True)
    # await state.finish()

