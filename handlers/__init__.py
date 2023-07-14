from aiogram import Dispatcher
from handlers.admin_handlers import register_admin_handlers
from handlers.common import register_start_handler
from handlers.user_handlers import register_user_handlers


def setup(dp: Dispatcher):
    register_admin_handlers(dp)
    register_start_handler(dp)
    register_user_handlers(dp)