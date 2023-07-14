from aiogram import Dispatcher
from handlers.admin_handlers.category_management.add_category_handler import ask_for_category_name_add, process_category_name_add, AddCategoryState
from handlers.admin_handlers.category_management.delete_category_handler import ask_for_category_name_delete, process_category_name_delete, DeleteCategoryState
from handlers.admin_handlers.category_management.get_categories_handler import get_categories_name


def setup_category_management_handlers(dp: Dispatcher):

    dp.register_callback_query_handler(ask_for_category_name_add, lambda c: c.data == 'add_category', state="*")
    dp.register_message_handler(process_category_name_add, state=AddCategoryState.waiting_for_category_name)

    dp.register_callback_query_handler(ask_for_category_name_delete, lambda c: c.data == 'delete_category')
    dp.register_message_handler(process_category_name_delete, state=DeleteCategoryState.waiting_for_category_name)

    dp.register_callback_query_handler(get_categories_name, lambda c: c.data == 'get_category')
