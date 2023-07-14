from aiogram.types import CallbackQuery
from keyboards import user_main_keyboard, user_profile_management_keyboard
from database.utils import get_user_balance


async def back_to_user_main_keyboard(callback_query: CallbackQuery):
    await callback_query.message.answer("Menu", reply_markup=user_main_keyboard)
    await callback_query.message.delete()


async def show_user_profile(callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    balance = await get_user_balance(user_id)
    message_text = f"Your balance: {balance}"
    await callback_query.message.answer(message_text, reply_markup=user_profile_management_keyboard)
    await callback_query.message.delete()