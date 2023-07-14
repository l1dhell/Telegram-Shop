from database import create_connection


async def delete_product_by_name(name: str):
    conn = await create_connection()

    await conn.execute(
        """
        DELETE FROM products
        WHERE name = $1
        """,
        name
    )

    await conn.close()