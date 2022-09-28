

async def create_address(address_collection, address):
    try:
        address = await address_collection.insert_many(address)
        adrs = []
        for address in address:
            address = await get_address(address_collection, address.inserted_id)
            adrs.append (address)
        return address
    except Exception as e:
        print(f'create_address.error: {e}')

async def get_address(address_collection, id):
    try:
        data = await address_collection.find_one({"_id": id})
        if data:
            return data
    except Exception as e:
        print(f'get_address.error: {e}')

async def get_all_addresses(address_collection, userId, skip, limit):
    try:
        address_cursor = address_collection.find({"userId": userId}).skip(int(skip)).limit(int(limit))
        address = await address_cursor.to_list(length=int(limit))
        return address
    except Exception as e:
        print(f'get_address.error: {e}')
        
async def delete_address(address_collection, address):
    try:
        result = await address_collection.delete_one({"_id": address["_id"]})
        if result.deleted_count > 0:
            return {'status': 'address deleted'}
        else:
             {'status': 'Nothing to delete'}
    except Exception as e:
        print(f'delete.error: {e}')
        
