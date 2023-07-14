from handlers.common.start_handler import start_handler

def register_start_handler(dp):
    dp.register_message_handler(start_handler, commands='start')