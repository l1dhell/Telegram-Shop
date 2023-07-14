from aiogram import Dispatcher
from handlers.admin_handlers.admin_handlers import back_to_admin_main_keyboard, show_bot_management,\
    show_shop_management, show_user_management, stop_bot_handler, back_to_user_management_keyboard,show_ban_management, show_database_options,\
    show_category_management, show_product_management, back_to_shop_management_keyboard
from handlers.admin_handlers.ban_management import setup_ban_management_handlers
from handlers.admin_handlers.category_management import setup_category_management_handlers
from handlers.admin_handlers.product_management import setup_product_management_handlers
from handlers.admin_handlers.product_link_management import setup_product_links_management_handlers


def register_admin_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(back_to_admin_main_keyboard, lambda c: c.data == "back_to_admin_main_keyboard")
    dp.register_callback_query_handler(back_to_user_management_keyboard, lambda c: c.data == "back_to_user_management_keyboard")
    dp.register_callback_query_handler(back_to_shop_management_keyboard, lambda c: c.data == "back_to_shop_management_keyboard")
    dp.register_callback_query_handler(show_bot_management, lambda c: c.data == "bot_management")
    dp.register_callback_query_handler(show_shop_management, lambda c: c.data == "shop_management")
    dp.register_callback_query_handler(show_user_management, lambda c: c.data == "user_management")
    dp.register_callback_query_handler(show_ban_management, lambda c: c.data == "ban_management")
    dp.register_callback_query_handler(show_category_management, lambda c: c.data == "category_management")
    dp.register_callback_query_handler(show_product_management, lambda c: c.data == "product_management")
    dp.register_callback_query_handler(show_database_options, lambda c: c.data == "database_options")
    dp.register_callback_query_handler(stop_bot_handler, lambda c: c.data == "bot_stop")

    setup_ban_management_handlers(dp)
    setup_category_management_handlers(dp)
    setup_product_management_handlers(dp)
    setup_product_links_management_handlers(dp)
