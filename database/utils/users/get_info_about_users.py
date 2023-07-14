import asyncpg
from data import DATABASE_URL


async def get_user_balance(telegram_id):
    conn = await asyncpg.connect(DATABASE_URL)
    user = await conn.fetchrow('SELECT * FROM users WHERE telegram_id = $1;', telegram_id)
    await conn.close()
    if user is None:
        return None
    return user['balance']


async def get_user_info(telegram_id):
    print("get_user_info")
    conn = await asyncpg.connect(DATABASE_URL)
    user = await conn.fetchrow('SELECT id, telegram_id, telegram_username, balance FROM users WHERE telegram_id = $1;', telegram_id)
    await conn.close()
    return user