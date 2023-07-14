from database import create_connection


async def get_product_links_count(product_id: int) -> int:
    conn = await create_connection()
    count = await conn.fetchval(
        "SELECT COUNT(*) FROM product_links WHERE product_id = $1",
        product_id
    )
    await conn.close()
    return count