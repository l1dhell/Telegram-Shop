import asyncpg
from database import create_connection


async def delete_info(user_id) -> None:
    conn = await create_connection()
    await conn.execute("DELETE FROM BANS WHERE user_id = $1", user_id)
    await conn.close()