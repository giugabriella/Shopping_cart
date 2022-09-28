import datetime
from bson.objectid import ObjectId
from src.models.order import (
    create_order,
    get_order,
    delete_order,
)
from src.models.order_item import (
    add_product,
    remove_product
)
from src.server.database import connect_db, db, disconnect_db


async def orders_crud():
   
    await connect_db()
    order_collection = db.order_collection
    order_item_collection = db.order_items_collection
    user = await db.users_collection.find_one({"email":"lu_domagalu@gmail.com"})
    order = None
    orderBuilder =  {
        "user": user["_id"],
        "price": 0, #duvida: como passar a soma dos valores dos produtos inseridos no carrinho?
        "address": "Rua Leg press, 45", #duvida: como passar o endereço vinculado ao usuário no carrinho carrinho?
        "paid": False,
        "create": datetime.datetime.now(),
        "authority": ""
    }

    while True:
        option = input("Entre com a opção de CRUD: ")
        if option == '1':
            # create order
            order = await create_order(
                order_collection,
                orderBuilder
            )
            print(order)
        elif option == '2':
            # get order
            id = ObjectId(input("Enter product code: "))
            order = await get_order(
                order_collection,
                id
            )
            print(order)
        elif option == '3':
            if order != None:
                result = await delete_order(
                    order_collection,
                    order
                )
                print(result)
            else:
                print("Please search a Order first")
           
        elif option == '4':
            '''add product to order'''
            order = await add_product(
                order_item_collection,
                int(input("Enter product code: ")),
                order
            )
            print(order)
        elif option == '5':
            '''remove product from order'''
            order = await remove_product(
                order_item_collection,
                int(input("Enter product code: ")),
                order
            )
            print("Produto removido!\n", order)
        elif option == '6':
            '''calculate the total price of the order'''
            print(order["price"])
        elif option == 'exit':
            break
        

    await disconnect_db()
