from pydantic import BaseModel, Field
from typing import Optional

class userProfile(BaseModel):
    name: str
    username: str = Field(min_length=6, max_length=10)
    password: str = Field(min_length=8, max_length=12)
    age: int = Field(default=18, ge=1)
    email: Optional[str] = None
    is_active: bool = False

class userProfileResponse(BaseModel):
    name: str
    username: str = Field(min_length=6, max_length=10)
    email: str
    is_active: bool