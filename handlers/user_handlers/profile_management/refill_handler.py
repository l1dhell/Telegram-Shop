from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from aiogram.types import CallbackQuery, PreCheckoutQuery
from database.utils.users import update_user_balance
from data import UKASSA_TOKEN
from loader import bot


class PaymentState(StatesGroup):
    waiting_for_amount = State()


async def refill_button_handler(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer("Отправьте сумму пополнения")
    await PaymentState.waiting_for_amount.set()


async def process_amount(message: types.Message, state: FSMContext):
    amount = int(message.text)
    async with state.proxy() as data:
        data['amount'] = amount
    payment_id = str(uuid.uuid4())
    create_payment(conn, message.from_user.id, amount, "yandex", payment_id)
    await bot.send_invoice(
        chat_id=message.chat.id,
        title="Пополнение баланса",
        description="Пополнение баланса на {} руб.".format(amount),
        provider_token=UKASSA_TOKEN,
        currency="RUB",
        is_flexible=False,
        prices=[types.LabeledPrice(label="Пополнение баланса", amount=amount * 100)],
        start_parameter="payment",
        payload=payment_id,
        need_name=True,
        need_phone_number=True,
        need_email=True,
        need_shipping_address=False,
    )


async def successful_payment(query: PreCheckoutQuery):
    payment_id = query.invoice_payload
    payment = get_payment(conn, query.from_user.id, amount, "yandex", payment_id)
    if payment['status'] != "PAID":
        update_payment_status(conn, query.from_user.id, amount, "yandex", payment_id, "CREATED", "PAID")
        await bot.answer_pre_checkout_query(query.id, ok=True)
        await bot.send_message(query.from_user.id, "Спасибо за оплату! Баланс успешно пополнен на {} руб.".format(payment['amount']))
    else:
        await bot.answer_pre_checkout_query(query.id, ok=False, error_message="Данный платеж уже был оплачен.")


async def cancel_payment(message: types.Message, state: FSMContext):
    await state.reset_state(with_data=False)
    await message.answer("Оплата отменена.")