from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.utils import get_all_products, get_link_to_product
from aiogram.types import CallbackQuery


async def get_products_to_store(callback_query: CallbackQuery):
    products = await get_all_products()
    buttons = []
    for product in products:
        button = InlineKeyboardButton(product['name'], callback_data=f"link_product_{product['id']}")
        buttons.append(button)
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    back_button = InlineKeyboardButton(text="Back", callback_data="back_to_product_management_keyboard_from_links")
    keyboard.add(back_button)
    await callback_query.message.answer("Choose product:", reply_markup=keyboard)


async def get_product_link(callback_query: CallbackQuery):
    product_id = int(callback_query.data.split("_")[-1])
    links = await get_link_to_product(product_id)

    if not links:
        await callback_query.answer("Sorry, the links for this product are not available.")
        return

    link_text = "\n".join(links)
    await callback_query.answer()
    await callback_query.message.answer(link_text)

































