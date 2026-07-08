from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional


class BlogBase(BaseModel):
    title: str
    description: Optional[str] = None
    author_name: str


class BlogCreate(BlogBase):
    pass


class BlogUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


class BlogResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    is_published: bool
    author_name: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
