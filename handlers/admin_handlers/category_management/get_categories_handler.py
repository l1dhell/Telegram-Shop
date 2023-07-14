from aiogram.types import CallbackQuery
from aiogram import types
from database.utils import get_categories
from keyboards import admin_category_management_keyboard


async def get_categories_name(callback_query: CallbackQuery):
    categories = await get_categories()
    categories_names = "\n".join([f"{category[0]} - {category[1]}" for category in categories])
    await callback_query.message.answer(categories_names, reply_markup=admin_category_management_keyboard)