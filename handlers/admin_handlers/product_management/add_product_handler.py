from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from decimal import Decimal
from keyboards import admin_shop_management_keyboard
from database.utils import add_product, get_categories
from aiogram.dispatcher.filters.state import State, StatesGroup


class AddProductState(StatesGroup):
    name = State()
    description = State()
    price = State()
    category = State()


async def add_product_handler(callback_query: types.CallbackQuery):
    await AddProductState.name.set()
    await callback_query.message.answer("Enter the *name* of the product", parse_mode="MarkdownV2")


async def name_handler(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await AddProductState.description.set()
    await message.answer("Enter the *description* of the product", parse_mode="MarkdownV2")


async def description_handler(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    await AddProductState.price.set()
    await message.answer("Enter the *price* of the product", parse_mode="MarkdownV2")


async def price_handler(message: types.Message, state: FSMContext):
    try:
        price = Decimal(message.text)
    except:
        await message.answer("Enter a valid price for the product (floating-point number)")
        return

    await state.update_data(price=price)
    await AddProductState.category.set()
    categories_list = await get_categories_list()
    await message.answer("Select the category of the product\n\n")
    await message.answer(categories_list)


async def category_handler(message: Message, state: FSMContext):
    try:
        category_id = int(message.text.split()[0])
    except:
        categories_list = await get_categories_list()
        await message.answer("Please select a *category* from the list below", reply_markup=ReplyKeyboardRemove(), parse_mode="MarkdownV2")
        await message.answer(categories_list)
        await AddProductState.category.set()
        return

    await state.update_data(category_id=category_id)
    data = await state.get_data()
    await add_product(category_id=data['category_id'], name=data['name'], description=data['description'],
                      price=data['price'], quantity=0)
    await message.answer("The *product* has been successfully added", reply_markup=admin_shop_management_keyboard, parse_mode="MarkdownV2")
    await state.reset_state()


async def category_selected_handler(message: Message, state: FSMContext):
    category_id = int(message.text)
    await state.update_data(category_id=category_id)
    data = await state.get_data()
    await add_product(category_id=data['category_id'], name=data['name'], description=data['description'], price=data['price'], quantity=0)
    await message.answer("The *product* has been successfully added", reply_markup=admin_shop_management_keyboard, parse_mode="MarkdownV2", disable_web_page_preview=True)
    await state.reset_state()


async def get_categories_list():
    categories = await get_categories()
    list_category = ""
    for category in categories:
        list_category += f"{category[0]}  {category[1]}\n"
    return list_category