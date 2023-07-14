from database import create_connection


async def add_category(name: str):
    conn = await create_connection()
    try:
        await conn.execute('INSERT INTO CATEGORIES (name) VALUES ($1)', name)
    finally:
        await conn.close()