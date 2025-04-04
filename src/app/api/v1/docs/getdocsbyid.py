from src.app.api.v1.docs.docs_router import get_router
from src.app.core.utils.error_handler import ErrorHandler

docs_router = get_router()

@docs_router.router.get("/doc_id")
async def get_doc_by_id(doc_id: str):
    try:
        doc = await docs_router.docs_service.get_doc_by_id(doc_id=doc_id)
        return ErrorHandler.handle_success(
            data={"doc": doc},
            message="document found"
        )
    except Exception as e:
        return ErrorHandler.handle_error(e)
    