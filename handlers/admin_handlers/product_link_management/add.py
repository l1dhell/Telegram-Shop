from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from database.utils import get_all_products, add_link_to_product
from loader import bot
from keyboards import admin_product_management_keyboard


class ProductLinksState(StatesGroup):
    links = State()
    confirm = State()


async def products_keyboard_callback_handler(callback_query: CallbackQuery, state: FSMContext):
    products = await get_all_products()
    buttons = []
    for product in products:
        button = InlineKeyboardButton(text=product['name'], callback_data=f"products_product_{product['id']}_{product['name']}")
        buttons.append(button)
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    back_button = InlineKeyboardButton(text="Back", callback_data="back_to_product_management_keyboard_from_links")
    keyboard.add(back_button)
    await callback_query.message.answer("Choose product:", reply_markup=keyboard)


async def product_links_callback_handler(callback_query: CallbackQuery, state: FSMContext):
    product_id = callback_query.data.split("_")[2]
    await bot.send_message(callback_query.message.chat.id, f"Please send me the links for product {product_id} separated by commas")
    await ProductLinksState.links.set()
    async with state.proxy() as data:
        data['product_id'] = product_id


async def product_links_receive_callback_handler(message, state: FSMContext):
    links = message.text.strip().split('\n')
    async with state.proxy() as data:
        product_id = data['product_id']
    await add_link_to_product(product_id, links)
    await bot.send_message(message.chat.id, "Links have been added to the product.")
    keyboard = admin_product_management_keyboard
    await bot.send_message(message.chat.id, "Product Management", reply_markup=keyboard)
    await state.finish()


async def product_links_add_callback_handler(callback_query: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        product_id = data['product_id']
        links = data['links']
    await add_link_to_product(product_id, links)
    await bot.send_message(callback_query.message.chat.id, f"Links have been added to product {product_id}")
    keyboard = admin_product_management_keyboard
    await callback_query.message.answer("Product Management", reply_markup=keyboard)
    await state.finish()


async def products_links_back_callback_handler(callback_query: CallbackQuery):
    await callback_query.message.answer("Product Management", reply_markup=admin_product_management_keyboard)

