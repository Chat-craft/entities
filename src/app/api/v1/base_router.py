from fastapi import APIRouter, Depends
from src.app.core.security.api_key_validator import validate_api_key


class BaseRouter:
    def __init__(self, prefix: str, tags: list[str]):
        self.router = APIRouter(
            prefix=prefix,
            tags=tags,  
            dependencies=[Depends(validate_api_key)]
        )
    
    def get_router(self) -> APIRouter:
        return self.router

