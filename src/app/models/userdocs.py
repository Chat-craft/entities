from pydantic import BaseModel, Field, ConfigDict
from typing import List
from app.models.document import Document


class UserDocs(BaseModel):
    user_id: str
    docs: List[Document] = Field(default_factory=list)  
    update_time : str
    model_config = ConfigDict(arbitrary_types_allowed=True) 
    


    