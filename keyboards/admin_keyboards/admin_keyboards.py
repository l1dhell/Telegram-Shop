from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def create_admin_main_keyboard():

    keyboard = InlineKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)

    button_user_management = InlineKeyboardButton("User Management", callback_data="user_management")
    button_bot_management = InlineKeyboardButton("Bot Management", callback_data="bot_management")
    button_shop_management = InlineKeyboardButton("Shop Management", callback_data="shop_management")
    button_database_options = InlineKeyboardButton("Database Options", callback_data="database_options")

    keyboard.row(button_user_management)
    keyboard.row(button_bot_management)
    keyboard.row(button_shop_management)
    keyboard.row(button_database_options)

    return keyboard


def create_admin_database_options_keyboard():

    keyboard = InlineKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)

    button_back = InlineKeyboardButton("Back", callback_data="back_to_admin_main_keyboard")

    keyboard.row(button_back)

    return keyboard


def create_admin_user_management_keyboard():

    keyboard = InlineKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)

    button_check_transactions = InlineKeyboardButton("Check transactions", callback_data="check_transactions")
    button_check_purchase = InlineKeyboardButton("Check Purchase", callback_data="check_purchase")
    button_delete_user = InlineKeyboardButton("Delete this user", callback_data="delete_user")
    button_ban_management = InlineKeyboardButton("Ban Management", callback_data="ban_management")
    button_all_information = InlineKeyboardButton("All Information", callback_data="all_information")
    button_back = InlineKeyboardButton("Back", callback_data="back_to_admin_main_keyboard")

    keyboard.row(button_check_transactions, button_check_purchase)
    keyboard.row(button_delete_user, button_ban_management)
    keyboard.row(button_all_information)
    keyboard.row(button_back)

    return keyboard


def create_admin_ban_management_keyboard():

    keyboard = InlineKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)

    button_ban_user = InlineKeyboardButton("Ban User", callback_data="ban_user")
    button_unban_user = InlineKeyboardButton("Unban User", callback_data="unban_user")
    button_check_ban = InlineKeyboardButton("Check Ban", callback_data="check_ban_user")
    button_back = InlineKeyboardButton("Back", callback_data="back_to_user_management_keyboard")

    keyboard.row(button_ban_user, button_unban_user)
    keyboard.row(button_check_ban)
    keyboard.row(button_back)

    return keyboard


def create_admin_shop_management_keyboard():

    keyboard = InlineKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)

    button_category_management = InlineKeyboardButton("Category Management", callback_data="category_management")
    button_product_management = InlineKeyboardButton("Product Management", callback_data="product_management")
    button_back = InlineKeyboardButton("Back", callback_data="back_to_admin_main_keyboard")

    keyboard.row(button_product_management, button_category_management)
    keyboard.row(button_back)

    return keyboard


def create_admin_product_management_keyboard():

    keyboard = InlineKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)

    button_add_product = InlineKeyboardButton("Add Product", callback_data="add_product")
    button_get_product = InlineKeyboardButton("Get Product", callback_data="get_product")
    button_delete_product = InlineKeyboardButton("Delete Product", callback_data="delete_product")
    button_add_products_to_store = InlineKeyboardButton("Add products links to the store", callback_data="add_products_to_store")
    button_get_products_to_store = InlineKeyboardButton("Get products links to the store", callback_data="get_products_to_store")
    button_back = InlineKeyboardButton("Back", callback_data="back_to_shop_management_keyboard")

    keyboard.row(button_add_product)
    keyboard.row(button_delete_product)
    keyboard.row(button_get_product)
    keyboard.row(button_add_products_to_store)
    keyboard.row(button_get_products_to_store)
    keyboard.row(button_back)

    return keyboard


def create_admin_category_management_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)

    button_add_category = InlineKeyboardButton("Add Category", callback_data="add_category")
    button_get_category = InlineKeyboardButton("Get Category", callback_data="get_category")
    button_delete_category = InlineKeyboardButton("Delete Category", callback_data="delete_category")
    button_back = InlineKeyboardButton("Back", callback_data="back_to_shop_management_keyboard")

    keyboard.row(button_add_category)
    keyboard.row(button_delete_category)
    keyboard.row(button_get_category)
    keyboard.row(button_back)

    return keyboard


def create_admin_bot_management_keyboard():

    keyboard = InlineKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)

    button_bot_stop = InlineKeyboardButton("Bot Stop", callback_data="bot_stop")
    button_back = InlineKeyboardButton("Back", callback_data="back_to_admin_main_keyboard")

    keyboard.row(button_bot_stop)
    keyboard.row(button_back)

    return keyboard
