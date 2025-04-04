from fastapi import FastAPI 
from contextlib import asynccontextmanager
from src.app.core.db.connect import ping_server
from src.app.crud.user.service import UserService
from src.app.crud.docs.service import DocsService
from src.app.crud.apikeys.service import ApiKeysService
from src.app.crud.user.repo import Repository
from src.app.crud.docs.repo import DocsRepo
from src.app.crud.apikeys.repo import ApiKeysRepo
from src.app.api.v1.users.user_router import UserRouter



@asynccontextmanager
async def lifespan(app: FastAPI):
    # load env 
    
    mongo_uri = "mongodb+srv://kunalkeshavsinghsahni:UUphn1xBC7JF6IS7@cluster0.rpxrqce.mongodb.net"

    # Initialize database connection
    client = await ping_server(mongo_uri)
    
    # Initialize repositories
    user_repo = Repository(client)
    docs_repo = DocsRepo(client)
    apikeys_repo = ApiKeysRepo(client)


    
    # Initialize services
    apikeys_service = ApiKeysService(apikeys_repo)
    docs_service = DocsService(docs_repo)
    user_service = UserService(user_repo, api_keys_service = apikeys_service, docs_service = docs_service)
    user_router = UserRouter(user_service=user_service)
   
    app.include_router(user_router.include_user_routes())

    
    yield

app = FastAPI(lifespan=lifespan)



