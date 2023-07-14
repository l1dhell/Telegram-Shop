from handlers.user_handlers.profile_management.purchases_handler import my_purchases_handler, switch_purchase, back_to_menu, PurchaseState


def setup_purchases_handler(dp):
    dp.register_callback_query_handler(my_purchases_handler, lambda c: c.data == 'my_purchases', state="*")
    dp.register_callback_query_handler(switch_purchase, lambda c: c.data in ['previous_purchase', 'next_purchase'], state=PurchaseState.PURCHASE_INFO)
    dp.register_callback_query_handler(back_to_menu, lambda c: c.data == 'back_to_main_menu', state=PurchaseState.PURCHASE_INFO)
    dp.register_message_handler(my_purchases_handler, lambda c: c.data == "my_purchases")