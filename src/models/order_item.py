
from src.server.database import db

async def add_product(order_item_collection, prodCode, order):
    '''metodo que adiciona produto no carrinho'''
    #buscando produto
    #inserindo orderItem
    #atualizando price na order
    #retorna order atualizada
    product = await db.product_collection.find_one({"code":prodCode})
    await order_item_collection.insert_one({"product":product["_id"], "order":order["_id"]})
    await db.order_collection.update_one({"_id":order["_id"]}, {'$inc':{"price": product["price"]}})

    return await db.order_collection.find_one({"_id":order["_id"]})

async def remove_product(order_item_collection, prodCode, order):
    '''metodo para remover produto do carrinho'''
    product = await db.product_collection.find_one({"code":prodCode})
    await order_item_collection.delete_one({"product":product["_id"], "order":order["_id"]})
    await db.order_collection.update_one({"_id":order["_id"]}, {'$inc':{"price": -product["price"]}})

    return await db.order_collection.find_one({"_id":order["_id"]})


    
    