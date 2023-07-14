from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from database.utils import check_ban
from keyboards import admin_main_keyboard


class CheckBanStates(StatesGroup):
    waiting_for_id_check_ban = State()


async def process_check_ban_callback(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer("Please enter the *Telegram ID* of the user you want to check:", parse_mode="MarkdownV2")
    await CheckBanStates.waiting_for_id_check_ban.set()


async def process_id_message(message: types.Message, state: FSMContext):
    telegram_id = message.text

    if await check_ban(int(telegram_id)):
        await message.answer("This *user* is banned.", reply_markup=admin_main_keyboard, parse_mode="MarkdownV2")
    else:
        await message.answer("This *user* is not banned.", reply_markup=admin_main_keyboard, parse_mode="MarkdownV2")

    await state.finish()


__all__ = ['process_check_ban_callback', 'process_id_message']

