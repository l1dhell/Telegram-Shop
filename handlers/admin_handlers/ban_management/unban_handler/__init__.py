from aiogram import Dispatcher
from handlers.admin_handlers.ban_management.unban_handler.unban_handler import process_unban_callback, process_id_message_unban, UnbanStates


def setup_unban_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(process_unban_callback, lambda c: c.data == "unban_user", state="*")
    dp.register_message_handler(process_id_message_unban, state=UnbanStates.waiting_for_id_unban)