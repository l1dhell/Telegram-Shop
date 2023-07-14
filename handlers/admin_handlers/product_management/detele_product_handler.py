from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram.types import Message
from keyboards import admin_shop_management_keyboard
from database.utils import delete_product_by_name
from aiogram.dispatcher.filters.state import State, StatesGroup


class DeleteProduct(StatesGroup):
    name = State()


async def get_name_product_handler(callback_query: CallbackQuery):
    await DeleteProduct.name.set()
    await callback_query.message.answer("Enter the *name* of the product for delete", parse_mode="MarkdownV2")


async def delete_product_name(message: Message, state: FSMContext):
    product_name = message.text
    deleted = await delete_product_by_name(product_name)
    if deleted:
        await message.answer(f"Product *{product_name}* has been deleted", parse_mode="MarkdownV2", reply_markup=admin_shop_management_keyboard)
    else:
        await message.answer(f"Product *{product_name}* not found or not deleted", parse_mode="MarkdownV2", reply_markup=admin_shop_management_keyboard)
    await state.finish()