from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from keyboards import user_main_keyboard
from database.utils import get_categories, get_products, update_user_balance, get_product_by_id, get_user_balance, delete_product_links, get_link_to_product, add_purchase, get_user_info
from loader import bot


class BuyProduct(StatesGroup):
    choosing_product = State()
    choosing_quantity = State()


async def catalog_callback_handler(callback_query: CallbackQuery):
    await callback_query.answer()
    categories = await get_categories()
    keyboard = InlineKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    for category in categories:
        keyboard.add(InlineKeyboardButton(category[1], callback_data=f"Category_{category[0]}"))
    keyboard.add(InlineKeyboardButton("Back", callback_data="Catalog_Back"))
    await bot.send_message(callback_query.from_user.id, "Choose a category", reply_markup=keyboard)


async def category_callback_handler(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.answer()
    category_id = int(callback_query.data.split("_")[1])
    products = await get_products(category_id)
    keyboard = InlineKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    for product in products:
        button_text = f"{product['name']} - {product['price']}"
        keyboard.add(InlineKeyboardButton(button_text, callback_data=f"Product_{product['id']}"))
    keyboard.add(InlineKeyboardButton("Back", callback_data="Back_to_categories"))
    await bot.send_message(callback_query.from_user.id, "Choose a product", reply_markup=keyboard)
    await state.update_data(category_id=category_id)


async def back_to_catalog_callback_handler(callback_query: CallbackQuery):
    await callback_query.answer()
    keyboard = user_main_keyboard
    await bot.send_message(callback_query.from_user.id, "Menu", reply_markup=keyboard)


async def back_to_categories_handler(callback_query: CallbackQuery):
    await callback_query.answer()
    categories = await get_categories()
    keyboard = InlineKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    for category in categories:
        keyboard.add(InlineKeyboardButton(category[1], callback_data=f"Category_{category[0]}"))
    keyboard.add(InlineKeyboardButton("Back", callback_data="Catalog_Back"))
    await bot.send_message(callback_query.from_user.id, "Choose a category", reply_markup=keyboard)


async def back_to_products_list_handler(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.answer()
    data = await state.get_data()
    category_id = data.get('category_id')
    if category_id is not None:
        products = await get_products(category_id)
        keyboard = InlineKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
        for product in products:
            button_text = f"{product['name']} - {product['price']}"
            keyboard.add(InlineKeyboardButton(button_text, callback_data=f"Product_{product['id']}"))
        keyboard.add(InlineKeyboardButton("Back", callback_data="Back_to_categories"))
        await bot.send_message(callback_query.from_user.id, "Choose a product", reply_markup=keyboard)
    else:
        await bot.send_message(callback_query.from_user.id, "You are not in any category. Please choose a category.")


async def product_callback_handler(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.answer()
    product_id = int(callback_query.data.split("_")[1])
    product = await get_product_by_id(product_id)
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Buy", callback_data=f"Buy_{product_id}"))
    keyboard.add(InlineKeyboardButton("Back", callback_data="Back_to_products_list"))
    await bot.send_message(callback_query.from_user.id, f"{product['name']}\n{product['description']}\nPrice: {product['price']}", reply_markup=keyboard)
    await state.update_data(product_id=product_id)


async def buy_callback_handler(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.answer()
    data = await state.get_data()
    product_id = data['product_id']
    user_id = callback_query.from_user.id
    quantity_keyboard = InlineKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=True).add(
        *[
            InlineKeyboardButton(str(i), callback_data=f"Quantity_{i}")
            for i in [1, 5, 10, 15, 20, 25, 50]
        ]
    )
    await bot.send_message(user_id, "Select quantity:", reply_markup=quantity_keyboard)
    await state.update_data(product_id=product_id)
    await BuyProduct.choosing_quantity.set()


async def quantity_callback_handler(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.answer()
    data = await state.get_data()
    product_id = data['product_id']
    quantity = int(callback_query.data.split("_")[1])
    telegram_id = callback_query.from_user.id

    user_balance = await get_user_balance(telegram_id)
    product = await get_product_by_id(product_id)
    links = await get_link_to_product(product_id)

    if quantity > len(links):
        quantity = len(links)

    total_price = product['price'] * quantity

    user_info = await get_user_info(telegram_id)
    user_id = user_info['id']

    if user_balance >= total_price:
        purchased_links = links[:quantity]
        await add_purchase(user_id, product_id, purchased_links)
        await delete_product_links(purchased_links)
        message_text = "Ссылки на купленные товары:\n" + "\n".join(purchased_links)
        await bot.send_message(telegram_id, message_text)

        await update_user_balance(telegram_id, total_price, action="-")
        await bot.send_message(telegram_id, f"{product['name']} bought",reply_markup=user_main_keyboard)
    else:
        await bot.send_message(telegram_id, "Insufficient balance. Please top-up your account.")
        keyboard = user_main_keyboard
        await bot.send_message(telegram_id, "Main menu", reply_markup=keyboard)

    await state.finish()