import asyncio
import logging
from aiogram import types
from db import create_table, create_correct_answers
from func import (dp, bot, cmd_start, cmd_quiz, right_answer,
                               wrong_answer, new_quiz, get_question, generate_options_keyboard)


logging.basicConfig(level=logging.INFO)


async def main():
    await create_table()
    await create_correct_answers()

    await dp.start_polling(bot)

    async def start(message: types.Message):
        await cmd_start(message)

    async def quiz(message: types.Message):
        await cmd_quiz(message)

    async def right_answer_wrapper(callback: types.CallbackQuery):
        await right_answer(callback)

    async def wrong_answer_wrapper(callback: types.CallbackQuery):
            await wrong_answer(callback)

    await new_quiz(message)
    await get_question(message, user_id)
    await generate_options_keyboard(answer_options, right_answer)


if __name__ == "__main__":
    asyncio.run(main())
