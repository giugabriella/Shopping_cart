
from src.schemas.product import ProductSchema

async def create_product(product_collection, product: ProductSchema):
    try:
        products = await product_collection.insert_many(product)
        prods = []
        for product in products:
            product = await get_product(product_collection, product.inserted_id)
            prods.append (product)
        return products
    except Exception as e:
        print(f'create_product.error: {e}')

async def get_product(product_collection, code):
    try:
        data = await product_collection.find_one({code})
        if data:
            return data
    except Exception as e:
        print(f'get_product.error: {e}')


async def delete_product(product_collection, code):
    try:
        product = await product_collection.delete_one(
            {'_id': code}
        )
        if product.deleted_count:
            return {'status': 'Product deleted'}
    except Exception as e:
        print(f'delete_product.error: {e}')