from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class BookmarkCreate(BaseModel):
    url: str
    title: str | None = None
    description: str | None = None

class BookmarkUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    is_favorite: bool | None = None

class BookmarkResponse(BaseModel):
    id: UUID
    user_id: UUID
    url: str
    title: str | None
    description: str | None
    is_favorite: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}