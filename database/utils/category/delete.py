from database import create_connection


async def delete_category(name: str):
    conn = await create_connection()
    try:
        category_id = await conn.fetchval('SELECT id FROM categories WHERE name = $1', name)
        await conn.execute('DELETE FROM products WHERE category_id = $1', category_id)
        await conn.execute('DELETE FROM categories WHERE name = $1', name)
    finally:
        await conn.close()