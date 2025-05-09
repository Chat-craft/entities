from fastapi import UploadFile, Form, File
from httpx import AsyncClient 
from src.app.crud.docs.service import DocsService
from src.app.models.document import Document
from src.app.models.doctype import DocType
from src.app.models.update_interval import UpdateInterval

class FileUploadService:
    def __init__(self, base_url : str, api_key : str, client : AsyncClient, docs_service : DocsService):
        self.client = client 
        self.base_url = base_url
        self.api_key = api_key
        self.docs_serive = docs_service
    
    async def upload_file(self, 
        user_id: str = Form(...),
        doc_name: str = Form(...),
        doc_type: str = Form(default=DocType.PDF.name),
        doc_url: str = Form(...),
        update_interval: str = Form(default=UpdateInterval.TIME_NONE),
        file: UploadFile = File(...)
        ):
        file_bytes = await file.read()
        files = {'file': (file.filename, file_bytes, file.content_type)}
        headers = {'x-api-key' : self.api_key, "user-id" : user_id}
        response = await self.client.post(
            f"{self.base_url}/upload/",
            files=files,
            headers=headers
        )
        #TODO: handle response status
        response.raise_for_status()
        #TODO: convert it into proper response model 
        # update db 
        doc = Document(
            doc_name=doc_name,
            doc_type=doc_type,
            doc_url=doc_url,
            update_interval=update_interval
        )
        await self.docs_serive.add_document(user_id=user_id, doc=doc)
        return response.json()



        

    