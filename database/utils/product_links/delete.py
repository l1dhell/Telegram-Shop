from database import create_connection
from typing import List


async def delete_product_links(links_to_delete: List[str]):
    conn = await create_connection()
    print(f"Удаляем ссылки на товары: {links_to_delete}")
    try:
        for link in links_to_delete:
            await conn.execute("DELETE FROM PRODUCT_linkS WHERE product_link = $1", link)
        print("Ссылки на товары успешно удалены из базы данных")
    except Exception as e:
        print(f"Ошибка при удалении ссылок на товары из базы данных: {e}")