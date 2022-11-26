from uuid import UUID
from datetime import datetime
from typing import Optional

from .users import User

from pydantic import(
    BaseModel, Field
)

class Tweets(BaseModel):
    tweets_id: UUID = Field(default=None)
    content: str = Field(
        ...,
        min_length=1,
        max_length=255
    )
    created_at: datetime = Field(default=datetime.now())
    update_at: Optional[datetime] = Field(default=None)
    by: User = Field(default=None)