from fastapi import HTTPException, Request, Header
from os import environ
from src.app.core.utils.status_codes import StatusCodes
from typing import Annotated


def validate_api_key(x_api_key: Annotated[str, Header()]):

    if x_api_key != "entities-api-key":
        raise HTTPException(status_code=StatusCodes.UNAUTHORIZED.value, detail="Invalid API key")


