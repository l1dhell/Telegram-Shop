from decimal import Decimal
from database import create_connection


async def add_product(category_id: int, name: str, description: str, price: int, quantity: int):
    conn = await create_connection()
    price_dec = Decimal(price).quantize(Decimal("0.01"))

    await conn.execute(
        """
        INSERT INTO products (category_id, name, description, price, quantity)
        VALUES ($1, $2, $3, $4, $5)
        """,
        category_id, name, description, price_dec, quantity
    )

    await conn.close()