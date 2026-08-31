from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    name: str
    photoUrl: Optional[str] = None
    role: str = "user"
    isActive: bool = True

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name: Optional[str] = None
    photoUrl: Optional[str] = None

class UserResponse(UserBase):
    id: str
    createdAt: datetime
    updatedAt: Optional[datetime] = None