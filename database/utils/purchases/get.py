from database import create_connection


async def get_user_purchases(user_id: int):
    print("get_user_purchases")
    conn = await create_connection()
    try:
        purchases = await conn.fetch(
            "SELECT p.id, pr.name as product_name, p.product_link, p.purchase_time FROM purchases p "
            "INNER JOIN products pr ON p.product_id = pr.id "
            "WHERE p.user_id = $1 "
            "ORDER BY p.purchase_time DESC",
            user_id
        )
        return purchases
    except Exception as e:
        print(f"Ошибка при получении информации о покупках пользователя: {e}")
    finally:
        await conn.close()