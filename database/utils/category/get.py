from database import create_connection


async def get_categories() -> list:
    conn = await create_connection()
    categories = await conn.fetch("SELECT id, name FROM categories")
    await conn.close()
    return [(category['id'], category['name']) for category in categories]