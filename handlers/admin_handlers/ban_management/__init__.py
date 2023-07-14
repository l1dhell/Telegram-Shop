from aiogram import Dispatcher
from handlers.admin_handlers.ban_management.ban_handler import setup_ban_handlers
from handlers.admin_handlers.ban_management.check_ban_handler import setup_check_ban_handlers
from handlers.admin_handlers.ban_management.unban_handler import setup_unban_handlers


def setup_ban_management_handlers(dp: Dispatcher):
    setup_unban_handlers(dp)
    setup_ban_handlers(dp)
    setup_check_ban_handlers(dp)
