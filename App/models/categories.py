from pydantic import BaseModel
from typing import Optional

class CategoryCreate(BaseModel):
    userId: str
    name: str
    icon: Optional[str] = None


class CategoryResponse(CategoryCreate):
    id: str