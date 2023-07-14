from database import create_connection


async def get_link_to_product(product_id: int):
    conn = await create_connection()

    async with conn.transaction():
        result = await conn.fetch("SELECT product_link FROM PRODUCT_links WHERE product_id = $1", product_id)

    await conn.close()

    links = [row['product_link'] for row in result]
    return links

