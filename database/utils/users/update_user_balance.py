from database import create_connection


async def update_user_balance(telegram_id, amount, action):
    conn = await create_connection()
    try:
        if action == "+":
            await conn.execute("UPDATE users SET balance = balance + $1 WHERE telegram_id = $2", amount, telegram_id)
        elif action == "-":
            await conn.execute("UPDATE users SET balance = balance - $1 WHERE telegram_id = $2", amount, telegram_id)
        else:
            raise ValueError("Invalid action: {}".format(action))
    finally:
        await conn.close()