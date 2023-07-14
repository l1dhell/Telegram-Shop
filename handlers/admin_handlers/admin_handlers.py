from aiogram.types import CallbackQuery
from keyboards import admin_main_keyboard, admin_user_management_keyboard,\
    admin_shop_management_keyboard, admin_bot_management_keyboard,\
    admin_ban_management_keyboard, admin_database_options_keyboard,\
    admin_product_management_keyboard, admin_category_management_keyboard


async def back_to_admin_main_keyboard(callback_query: CallbackQuery):
    await callback_query.message.answer("ADMIN PANEL:", reply_markup=admin_main_keyboard)
    await callback_query.message.delete()


async def back_to_user_management_keyboard(callback_query: CallbackQuery):
    await callback_query.message.answer("User Management", reply_markup=admin_user_management_keyboard)
    await callback_query.message.delete()


async def back_to_shop_management_keyboard(callback_query: CallbackQuery):
    await callback_query.message.answer("Shop Management", reply_markup=admin_shop_management_keyboard)
    await callback_query.message.delete()


async def show_database_options(callback_query: CallbackQuery):
    await callback_query.message.answer("Database Options", reply_markup=admin_database_options_keyboard)
    await callback_query.message.delete()


async def show_bot_management(callback_query: CallbackQuery):
    await callback_query.message.answer("Bot Management", reply_markup=admin_bot_management_keyboard)
    await callback_query.message.delete()


async def show_category_management(callback_query: CallbackQuery):
    await callback_query.message.answer("Category Management", reply_markup=admin_category_management_keyboard)
    await callback_query.message.delete()


async def show_product_management(callback_query: CallbackQuery):
    await callback_query.message.answer("Product Management", reply_markup=admin_product_management_keyboard)
    await callback_query.message.delete()


async def show_shop_management(callback_query: CallbackQuery):
    await callback_query.message.answer("Shop Management", reply_markup=admin_shop_management_keyboard)
    await callback_query.message.delete()


async def show_user_management(callback_query: CallbackQuery):
    await callback_query.message.answer("User Management", reply_markup=admin_user_management_keyboard)
    await callback_query.message.delete()


async def show_ban_management(callback_query: CallbackQuery):
    await callback_query.message.answer("Ban Management", reply_markup=admin_ban_management_keyboard)
    await callback_query.message.delete()


async def stop_bot_handler(callback_query: CallbackQuery):
    await callback_query.message.answer("Bot stop")
    await callback_query.bot.close()
    await callback_query.message.delete()
