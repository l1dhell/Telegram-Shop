from aiogram import Dispatcher
from handlers.admin_handlers.product_management.add_product_handler import name_handler, description_handler, price_handler, category_handler, AddProductState, add_product_handler
from handlers.admin_handlers.product_management.detele_product_handler import delete_product_name, DeleteProduct, get_name_product_handler
from handlers.admin_handlers.product_management.get_product_handler import get_products_callback, select_product_callback, back_to_products_callback, back_to_admin_product_management_callback


def setup_product_management_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(add_product_handler, lambda c: c.data == "add_product")
    dp.register_message_handler(name_handler, state=AddProductState.name)
    dp.register_message_handler(description_handler, state=AddProductState.description)
    dp.register_message_handler(price_handler, state=AddProductState.price)
    dp.register_message_handler(category_handler, state=AddProductState.category)

    dp.register_callback_query_handler(get_name_product_handler, lambda c: c.data == "delete_product")
    dp.register_message_handler(delete_product_name, state=DeleteProduct.name)

    dp.register_callback_query_handler(get_products_callback, lambda c: c.data == "get_product")
    dp.register_callback_query_handler(select_product_callback, lambda c: c.data.startswith("product_"))
    dp.register_callback_query_handler(back_to_products_callback, lambda c: c.data == "back_to_products")
    dp.register_callback_query_handler(back_to_admin_product_management_callback, lambda c: c.data == "back_product_management_keyboard")
