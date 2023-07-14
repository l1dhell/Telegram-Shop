from database import create_connection
from typing import List


async def add_link_to_product(product_id: int, links: List[str]):
    conn = await create_connection()
    async with conn.transaction():
        for link in links:
            await conn.execute("INSERT INTO PRODUCT_links (product_id, product_link) VALUES ($1, $2)", int(product_id), link)
    await conn.close()