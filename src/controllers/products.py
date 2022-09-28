
from src.models.product import (
    create_product,
    get_product,
    delete_product
)
from src.server.database import connect_db, db, disconnect_db


async def products_crud():
    
    
    await connect_db()
    product_collection = db.product_collection

    product =  [{
        "name": "Creatina",
        "description": "Pozinho dos Deuses",
        "price": 80.00,
        "code": 31415926
    },
    {
        "name": "whey protey ultra 89g protein",
        "description": "Proteina da malásia pré histórica sem açucar",
        "price": 100.00,
        "code": 31415930
    }]
    while True:
        option = input("Entre com a opção de CRUD: ")
        if option == '1':
            # create product
            products = await create_product(
                product_collection,
                product
            )
            print(products)
        elif option == '2':
            # get product
            user = await get_product(
                product_collection,
                product["code"]
            )
            print(user)
        elif option == '3':
            # delete product
            user = await get_product(
                product_collection,
                product["code"]
            )

            result = await delete_product(
                product_collection,
                product["code"]
            )
            print(result)
        elif option == 'exit':
            break
 
    await disconnect_db()
