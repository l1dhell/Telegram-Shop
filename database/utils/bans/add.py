from database import create_connection


async def add_info(telegram_id: int, ban_reason: str) -> None:
    conn = await create_connection()
    try:
        await conn.execute("INSERT INTO BANS (user_id, reason) VALUES ($1, $2)", int(telegram_id), ban_reason)
    finally:
        await conn.close()