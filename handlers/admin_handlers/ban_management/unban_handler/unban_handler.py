from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from database.utils import delete_info, check_ban
from keyboards import admin_main_keyboard


class UnbanStates(StatesGroup):
    waiting_for_id_unban = State()


async def process_unban_callback(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer("Please enter the *Telegram ID* of the user you want to unban:", parse_mode="MarkdownV2")
    await UnbanStates.waiting_for_id_unban.set()


async def process_id_message_unban(message: types.Message, state: FSMContext):
    telegram_id = message.text

    if not await check_ban(int(telegram_id)):
        await message.answer("This *user* is not banned.", reply_markup=admin_main_keyboard, parse_mode="MarkdownV2")
        await state.finish()
        return

    await delete_info(int(telegram_id))
    await message.answer(f"User *{telegram_id}* has been unbanned.", reply_markup=admin_main_keyboard, parse_mode="MarkdownV2")
    await state.finish()

__all__ = ['process_unban_callback', 'process_id_message_unban']