from aiogram import Dispatcher
from handlers.admin_handlers.ban_management.ban_handler.ban_handler import process_ban_callback, process_id_message, process_reason_message, BanStates


def setup_ban_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(process_ban_callback, lambda c: c.data == "ban_user", state="*")
    dp.register_message_handler(process_id_message, state=BanStates.waiting_for_id)
    dp.register_message_handler(process_reason_message, state=BanStates.waiting_for_reason)