from fastapi import Depends
from src.app.api.v1.base_router import BaseRouter
from src.app.crud.docs.service import DocsService
from src.app.core.utils.singleton import Singleton


class DocsRouter(BaseRouter, metaclass = Singleton):
    def __init__(self, docs_service: DocsService = Depends(DocsService)):
        super().__init__(
            prefix="/v1/docs",
            tags=["docs"]
        )
        self.docs_service = docs_service
