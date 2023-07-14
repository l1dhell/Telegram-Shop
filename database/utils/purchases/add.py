from datetime import datetime
from database import create_connection
from typing import List


async def add_purchase(user_id: int, product_id: int, product_links: List[str]):
    conn = await create_connection()
    try:
        purchase_time = datetime.utcnow()
        await conn.execute(
            "INSERT INTO PURCHASES (user_id, product_id, product_link, purchase_time) VALUES ($1, $2, $3, $4)",
            user_id, product_id, product_links, purchase_time
        )
        print("Информация о покупке успешно добавлена в базу данных")
    except Exception as e:
        print(f"Ошибка при добавлении информации о покупке в базу данных: {e}")
    finally:
        await conn.close()