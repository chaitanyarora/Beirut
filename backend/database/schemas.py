from pydantic import BaseModel, Field
from typing import Optional

class ItemSchema(BaseModel):
    name: str = Field(..., example="Sample Item")
    description: Optional[str] = Field(None, example="This is a sample item")

class UpdateItemSchema(BaseModel):
    name: Optional[str] = Field(None, example="Updated Item")
    description: Optional[str] = Field(None, example="Updated description")
