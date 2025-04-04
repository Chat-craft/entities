from src.app.models.apikeys import ApiKeys
from motor.motor_asyncio import AsyncIOMotorClient


class ApiKeysRepo:
    def __init__(self, client: AsyncIOMotorClient):
        self.collection = client.get_database("test_d").get_collection("api_keys")
        

    async def create_api_key(self, api_key: ApiKeys):
        try:
            api_key = await self.collection.insert_one(api_key.model_dump()) 
            return api_key
        except Exception as e:
            raise e 
        
    async def get_api_key(self, api_key: ApiKeys):
        try:
            api_key = await self.collection.find_one({"api_key": api_key.api_key})
            return api_key
        except Exception as e:
            raise e 
        
    async def get_api_key_by_user_id(self, user_id: str):
        try:
            api_key = await self.collection.find_one({"user_id": user_id})
            return api_key
        except Exception as e:
            raise e 
        