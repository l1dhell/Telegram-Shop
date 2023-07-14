from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from database.utils import get_user_info, get_user_purchases
from keyboards import user_profile_management_keyboard
from loader import bot


class PurchaseStates(StatesGroup):
    PURCHASES_LIST = State()
    PURCHASE_INFO = State()


async def my_purchases_handler(callback_query: CallbackQuery, state: FSMContext):
    telegram_id = callback_query.from_user.id

    user_info = await get_user_info(telegram_id)
    user_id = user_info['id']

    purchases = await get_user_purchases(user_id)
    num_purchases = len(purchases)

    if num_purchases == 0:
        await callback_query.answer("You have no purchases yet.")
        return

    purchases = sorted(purchases, key=lambda p: p['purchase_time'])

    if num_purchases < 3:
        for purchase in purchases:
            message_text = f"Product name: {purchase['product_name']}\nPurchase time: {purchase['purchase_time']}"
            await callback_query.message.answer(message_text)
        keyboard = user_profile_management_keyboard()
        await callback_query.message.answer("Back to main menu", reply_markup=keyboard)
        await state.finish()
    else:
        current_purchase_index = 0
        await show_purchase_info(callback_query.message, purchases[current_purchase_index])
        keyboard = get_purchase_switch_keyboard(current_purchase_index, num_purchases)
        await bot.send_message(callback_query.from_user.id, "Use arrows to switch between your purchases", reply_markup=keyboard)
        await state.update_data(purchases=purchases, current_purchase_index=current_purchase_index)
        await PurchaseStates.PURCHASE_INFO.set()


def get_purchase_switch_keyboard(current_purchase_index: int, num_purchases: int) -> InlineKeyboardMarkup:
    buttons = []
    if current_purchase_index > 0:
        buttons.append(InlineKeyboardButton("<", callback_data="previous_purchase"))
    if current_purchase_index < num_purchases - 1:
        buttons.append(InlineKeyboardButton(">", callback_data="next_purchase"))
    buttons.append(InlineKeyboardButton("Back", callback_data="back_to_main_menu"))
    keyboard = InlineKeyboardMarkup(row_width=3)
    keyboard.add(*buttons)
    return keyboard


async def show_purchase_info(message, purchase):
    message_text = f"Product name: {purchase['product_name']}\nPurchase time: {purchase['purchase_time']}"
    await message.answer(message_text)


async def switch_purchase(callback_query: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    purchases = data.get("purchases")
    current_purchase_index = data.get("current_purchase_index")
    if callback_query.data == "next_purchase":
        current_purchase_index += 1
    elif callback_query.data == "previous_purchase":
        current_purchase_index -= 1

    await show_purchase_info(callback_query.message, purchases[current_purchase_index])
    keyboard = get_purchase_switch_keyboard(current_purchase_index, len(purchases))
    await callback_query.message.edit_reply_markup(reply_markup=keyboard)

    await state.update_data(current_purchase_index=current_purchase_index)


async def back_to_menu(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.answer()
    keyboard = user_profile_management_keyboard()
    await callback_query.message.answer("Back to main menu", reply_markup=keyboard)
    await state.finish()


