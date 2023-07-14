from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def create_user_main_keyboard():

    keyboard = InlineKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)

    button_my_profile = InlineKeyboardButton("My Profile", callback_data="my_profile")
    button_catalog = InlineKeyboardButton("Catalog", callback_data="Catalog")
    button_help = InlineKeyboardButton("Help", url="https://t.me/Ai_digi_digi_dai", callback_data="help")

    keyboard.row(button_catalog, button_my_profile)
    keyboard.add(button_help)

    return keyboard


def create_user_profile_management_keyboard():

    keyboard = InlineKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)

    button_my_transactions = InlineKeyboardButton("My transactions", callback_data="my_transactions")
    button_my_purchases = InlineKeyboardButton("My purchases", callback_data="my_purchases")
    button_my_replenish_account = InlineKeyboardButton("Refill", callback_data="Refill")
    button_back = InlineKeyboardButton("Back", callback_data="back_to_user_main_keyboard")

    keyboard.row(button_my_purchases, button_my_transactions)
    keyboard.row(button_my_replenish_account)
    keyboard.row(button_back)

    return keyboard
