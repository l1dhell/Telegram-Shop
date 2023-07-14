from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram import types
from database.utils import delete_category, get_categories
from keyboards import admin_shop_management_keyboard


class DeleteCategoryState(StatesGroup):
    waiting_for_category_name = State()


async def ask_for_category_name_delete(callback_query: CallbackQuery):
    categories = await get_categories()
    categories_text = "\n".join([f"{category[1]}" for category in categories])
    await callback_query.message.answer(f"List categories:\n{categories_text}")
    await callback_query.message.answer("Send me category name:")
    await DeleteCategoryState.waiting_for_category_name.set()


async def process_category_name_delete(message: types.Message, state: FSMContext):
    category_name = message.text
    if not await check_category_exists(category_name):
        await message.answer(f"Category {category_name} does not exist!")
    else:
        await delete_category(category_name)
        await state.finish()
        await message.answer(f"Category {category_name} has been deleted!",reply_markup=admin_shop_management_keyboard)


async def check_category_exists(category_name: str):
    categories = await get_categories()
    return any(category_name == category[1] for category in categories)