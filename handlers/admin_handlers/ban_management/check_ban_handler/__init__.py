from aiogram import Dispatcher
from handlers.admin_handlers.ban_management.check_ban_handler.check_ban_handler import process_check_ban_callback, process_id_message, CheckBanStates


def setup_check_ban_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(process_check_ban_callback, lambda c: c.data == "check_ban_user")
    dp.register_message_handler(process_id_message, state=CheckBanStates.waiting_for_id_check_ban)