import asyncpg
from database import create_connection


async def check_ban(user_id):
    ban_info = None

    try:
        conn = await create_connection()
        ban_info = await conn.fetchrow("""
            SELECT * FROM BANS WHERE user_id = $1
        """, user_id)
    except asyncpg.exceptions.PostgresError as e:
        print(f"Error '{e}' occurred")
    finally:
        await conn.close()

    if not ban_info:
        return None

    return ban_info