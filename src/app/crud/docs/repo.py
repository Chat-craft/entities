from src.app.models.userdocs import UserDocs
from motor.motor_asyncio import AsyncIOMotorClient
from src.app.models.document import Document
from typing import List
from src.app.models.doctype import DocType
from datetime import datetime

class DocsRepo:
    def __init__(self, client: AsyncIOMotorClient):
        self.collection = client.get_database("test_d").get_collection("userdocs")


    async def create_doc(self, doc: Document) -> Document | Exception :
        try:
            doc = await self.collection.insert_one(doc.model_dump())
            return Document.model_validate(doc)
        except Exception as e:
            raise e 
        
    async def get_doc_by_id(self, doc_id: str) -> Document | Exception :
        try:
            doc = await self.collection.find_one({"doc_id": doc_id})
            if not doc : return None
            return Document.model_validate(doc)
        except Exception as e:
            raise e 

    async def get_all_docs(self) -> List[Document] | Exception :
        try:
            docs = await self.collection.find().to_list(length=100)
            res = []
            for doc in docs:
                res.append(Document.model_validate(doc))
            return res
        except Exception as e:
            raise e 
        
    async def update_doc(self, doc_id: str, doc: Document) -> Document | Exception :
        try:
            doc = await self.collection.update_one({"doc_id": doc_id}, {"$set": doc.model_dump()})
            if not doc : return None
            return Document.model_validate(doc)
        except Exception as e:
            raise e 
        
    async def delete_doc(self, doc_id: str) -> Document | Exception :
        try:
            doc = await self.collection.delete_one({"doc_id": doc_id})
            if not doc : return None
            return Document.model_validate(doc)  
        except Exception as e:
            raise e 
        
    async def get_docs_by_user_id(self, user_id: str) -> List[Document] | Exception :
        try:
            docs = await self.collection.find({"user_id": user_id}).to_list(length=100)   
            if not docs: return None 
            res = []
            for doc in docs: res.append(Document.model_validate(doc))
            return res
        except Exception as e:
            raise e 
        
    async def get_docs_by_doc_id(self, doc_id: str) -> Document | Exception :
        try:
            doc = await self.collection.find_one({"doc_id": doc_id})
            if not doc : return None
            return Document.model_validate(doc)
        except Exception as e:
            raise e 
        
    async def get_docs_by_doc_name(self, doc_name: str) -> Document | Exception :
        try:
            doc = await self.collection.find_one({"doc_name": doc_name})
            if not doc : return None
            return Document.model_validate(doc)
        except Exception as e:
            raise e 
        
    async def get_docs_by_doc_type(self, doc_type: DocType) -> List[Document] | Exception :
        try:
            docs = await self.collection.find({"doc_type": doc_type}).to_list(length=100)
            if not docs : return None 
            res = []
            for doc in docs : res.append(Document.model_validate(doc))
            return res
        except Exception as e:
            raise e 
        
    async def get_docs_by_doc_url(self, doc_url: str) -> Document | Exception :
        try:
            doc = await self.collection.find_one({"doc_url": doc_url})
            if not doc : return None
            return Document.model_validate(doc)
        except Exception as e:
            raise e     
    
    async def get_docs_by_doc_created_at(self, doc_created_at: datetime) -> List[Document] | Exception :
        try:
            docs = await self.collection.find({"doc_created_at": doc_created_at}).to_list(length=100)
            if not docs : return None 
            res = []
            for doc in docs: res.append(Document.model_validate(doc))
            return res
        except Exception as e:
            raise e 

    async def get_docs_by_doc_updated_at(self, doc_updated_at: datetime) -> List[Document] | Exception :
        try:
            docs = await self.collection.find({"doc_updated_at": doc_updated_at}).to_list(length=100)
            if not docs : return [] 
            res = []
            for doc in docs: res.append(Document.model_validate(doc))
            return res
        except Exception as e:
            raise e 
                    
    async def get_docs_by_user_id_and_status(self, user_id: str, status: bool) -> List[Document] | Exception:
        try:
            docs = await self.collection.find({
                "user_id": user_id,
                "status": status
            }).to_list(length=100)
            res = []
            for doc in docs:
                res.append(Document.model_validate(doc))
            return res

        except Exception as e:
            raise e