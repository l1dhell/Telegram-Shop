from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from database.utils import add_info, check_ban
from keyboards import admin_main_keyboard


class BanStates(StatesGroup):
    waiting_for_id = State()
    waiting_for_reason = State()


async def process_ban_callback(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer("Please enter the *Telegram ID* of the user you want to ban:", parse_mode="MarkdownV2")
    await BanStates.waiting_for_id.set()


async def process_id_message(message: types.Message, state: FSMContext):

    telegram_id = message.text

    if await check_ban(int(telegram_id)):
        await message.answer("This *user* is already banned.", reply_markup=admin_main_keyboard, parse_mode="MarkdownV2")
        await state.finish()
        return

    await state.update_data(telegram_id=telegram_id)
    await message.answer("Please enter the *reason* for the ban:", parse_mode="MarkdownV2")
    await BanStates.waiting_for_reason.set()


async def process_reason_message(message: types.Message, state: FSMContext):
    data = await state.get_data()
    telegram_id = data.get('telegram_id')
    await add_info(telegram_id, message.text)
    await message.answer(f"User *{telegram_id}* has been banned for the following reason: {message.text}", reply_markup=admin_main_keyboard, parse_mode="MarkdownV2")
    await state.finish()

__all__ = ['process_ban_callback', 'process_id_message', 'process_reason_message']