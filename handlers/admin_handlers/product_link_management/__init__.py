from aiogram import Dispatcher
from handlers.admin_handlers.product_link_management.add import products_keyboard_callback_handler, product_links_callback_handler, products_links_back_callback_handler,product_links_receive_callback_handler,product_links_add_callback_handler, ProductLinksState
from handlers.admin_handlers.product_link_management.get import get_products_to_store,get_product_link


def setup_product_links_management_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(products_keyboard_callback_handler, lambda c: c.data == "add_products_to_store")
    dp.register_callback_query_handler(product_links_callback_handler, lambda c: c.data.startswith("products_product_"))
    dp.register_callback_query_handler(products_links_back_callback_handler, lambda c: c.data == "back_to_product_management_keyboard_from_links")
    dp.register_message_handler(product_links_receive_callback_handler, state=ProductLinksState.links)
    dp.register_callback_query_handler(product_links_add_callback_handler, lambda c: c.data == "confirm_product_links", state=ProductLinksState.confirm)

    dp.register_callback_query_handler(get_products_to_store, lambda c: c.data == "get_products_to_store")
    dp.register_callback_query_handler(get_product_link, lambda c: c.data.startswith("link_product_"))