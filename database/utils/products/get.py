from database import create_connection


async def get_product_by_id(product_id: int) -> dict:
    conn = await create_connection()
    try:
        product = await conn.fetchrow("SELECT * FROM products WHERE id = $1", product_id)
        if product:
            return dict(product)
        else:
            return None
    finally:
        await conn.close()


async def get_products(category_id: int) -> list:
    conn = await create_connection()
    products = await conn.fetch("SELECT * FROM products WHERE category_id = $1", category_id)
    await conn.close()
    return products


async def get_all_products() -> list:
    conn = await create_connection()
    products = await conn.fetch("SELECT * FROM products")
    await conn.close()
    all_products = []
    for product in products:
        product_id = product['id']
        product_name = product.get('name', 'None')
        product_description = product.get('description', 'None')
        product_price = product.get('price', 'None')
        all_products.append({'id': product_id, 'name': product_name, 'description': product_description, 'price': product_price})
    return all_products