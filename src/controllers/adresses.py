
from src.models.address import (
    create_address,
    get_address,
    delete_address,
    get_all_addresses
)
from bson.objectid import ObjectId
from src.server.database import connect_db, db, disconnect_db


async def address_crud():
    await connect_db()
    address_collection = db.address_collection
    address = None
    user = await db.users_collection.find_one({"email":"lu_domagalu@gmail.com"})
    addressBuilder = [{
        "userId": user['_id'],
        "street": "rua leg press, 45",
        "cep": "00000-000",
        "district": "Smart fit",
        "city": "Gym",
        "state": "Body Builder",
        "is_delivery": False
    }]
    
    while True:
        option = input("Entre com a opção de CRUD: ")
        if option == '1':
            # create address
            address = await create_address(
                address_collection,
                addressBuilder
            )
            print(address)
        elif option == '2':
            # get address
            id = input("Enter the adress ID: ")
            address = await get_address(
                address_collection,
                ObjectId(id)
            )
            print(address)
        elif option == '3':
            if address != None:
                result = await delete_address(
                    address_collection,
                    address
                )
                print(result)
            else:
                print("Please search a Order first")
        elif option == '4': 
            result = await get_all_addresses(
                address_collection,
                user['_id'],
                0,
                10000
            )
            print(result)
        elif option == 'exit':
            break
 
    await disconnect_db()
