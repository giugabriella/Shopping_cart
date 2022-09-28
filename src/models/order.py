
from src.schemas.order import OrderSchema
from src.server.database import connect_db, db, disconnect_db

async def create_order(order_collection, order):
    try:
        order = await order_collection.insert_one(order)
        
        if order.inserted_id:
            order = await get_order(order_collection, order.inserted_id)
            return order
    except Exception as e:
        print(order_collection)
        print(order_collection["user"])
        print(f'create_order.error: {e}')
    
async def get_order(order_collection, order):
    try: 
        data = await order_collection.find_one({"_id":order})
        if data:
            return data 
    except Exception as e:
        print(f'get_order.error: {e}')
        
async def delete_order(order_collection, order):
    try:
        result = await order_collection.delete_one({"_id":order["_id"]})
        if result.deleted_count > 0:
            await db.order_items_collection.delete_many({"order":order["_id"]})
            return {'status': 'Order deleted'}
    except Exception as e:
        print(f'delete.error: {e}')