from aiogram import Dispatcher
from handlers.user_handlers.user_handlers import back_to_user_main_keyboard, show_user_profile
from handlers.user_handlers.catalog_keyboard_constructor import catalog_callback_handler, category_callback_handler, back_to_catalog_callback_handler,\
    product_callback_handler, buy_callback_handler, quantity_callback_handler, BuyProduct, back_to_categories_handler, back_to_products_list_handler


def register_user_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(back_to_user_main_keyboard, lambda c: c.data == "back_to_user_main_keyboard")
    dp.register_callback_query_handler(show_user_profile, lambda c: c.data == "my_profile")
    dp.register_callback_query_handler(catalog_callback_handler, text="Catalog")
    dp.register_callback_query_handler(category_callback_handler, lambda c: c.data.startswith("Category"), state="*")
    dp.register_callback_query_handler(product_callback_handler, lambda c: c.data.startswith("Product_"), state="*")
    dp.register_callback_query_handler(buy_callback_handler, lambda c: c.data.startswith("Buy_"), state="*", run_task=True)
    dp.register_callback_query_handler(quantity_callback_handler, lambda c: c.data.startswith("Quantity_"), state=BuyProduct.choosing_quantity, run_task=True)
    dp.register_callback_query_handler(back_to_categories_handler, lambda c: c.data == "Back_to_categories")
    dp.register_callback_query_handler(back_to_products_list_handler, lambda c: c.data == "Back_to_products_list")
    dp.register_callback_query_handler(back_to_catalog_callback_handler, lambda c: c.data == "Catalog_Back", state="*")