from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from database.utils import get_all_products
from keyboards import admin_product_management_keyboard


async def get_products_callback(callback_query: CallbackQuery):
    products = await get_all_products()
    keyboard = InlineKeyboardMarkup()
    back_button = InlineKeyboardButton("Back", callback_data="back_product_management_keyboard")
    keyboard.row(back_button)

    for product in products:
        product_id = product["id"]
        product_name = product["name"]
        product_callback_data = f"product_{product_id}"
        product_button = InlineKeyboardButton(product_name, callback_data=product_callback_data)
        keyboard.row(product_button)
    await callback_query.message.answer("Choose a product:", reply_markup=keyboard)


async def select_product_callback(callback_query: CallbackQuery):
    product_id = int(callback_query.data.split("_")[1])
    products = await get_all_products()

    for product in products:
        if product["id"] == product_id:
            product_name = product.get("name", "None")
            product_description = product.get("description", "None")
            product_price = product.get("price", "None")
            product_info_text = f"Name: {product_name}\n\nDescription: {product_description}\n\nPrice: {product_price}"
            break

    keyboard = InlineKeyboardMarkup()
    back_button = InlineKeyboardButton("Back", callback_data="back_to_products")
    keyboard.row(back_button)

    await callback_query.message.answer(product_info_text, reply_markup=keyboard)


async def back_to_admin_product_management_callback(callback_query: CallbackQuery):
    await callback_query.message.answer("Product Management", reply_markup=admin_product_management_keyboard)


async def back_to_products_callback(callback_query: CallbackQuery):
    products = await get_all_products()
    keyboard = InlineKeyboardMarkup()
    back_button = InlineKeyboardButton("Back", callback_data="back_to_categories")
    keyboard.row(back_button)

    for product in products:
        product_id = product["id"]
        product_name = product["name"]
        product_callback_data = f"product_{product_id}"
        product_button = InlineKeyboardButton(product_name, callback_data=product_callback_data)
        keyboard.row(product_button)
    await callback_query.message.answer("Choose a product:", reply_markup=keyboard)