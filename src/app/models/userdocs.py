from pydantic import BaseModel, Field, ConfigDict
from bson import ObjectId
from typing import List
from app.models.document import Document


class UserDocs(BaseModel):
    user_id: ObjectId = Field(default_factory=ObjectId)
    docs: List[Document] = Field(default_factory=list)  
    model_config = ConfigDict(arbitrary_types_allowed=True) 


