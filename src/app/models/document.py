from pydantic import BaseModel, ConfigDict
from bson import ObjectId
from pydantic import Field
from datetime import datetime, timezone
from src.app.models.doctype import DocType


class Document(BaseModel):
    doc_id : ObjectId = Field(default_factory=ObjectId)
    doc_name : str = Field(max_length=255)
    doc_type : DocType = Field(default=DocType.PDF)
    doc_url : str = Field(max_length=300)   
    doc_created_at : datetime = Field(default_factory= lambda : datetime.now(timezone.utc))
    doc_updated_at : datetime = Field(default_factory= lambda : datetime.now(timezone.utc))
    doc_status : bool = Field(default=True)
    model_config = ConfigDict(arbitrary_types_allowed=True) 




