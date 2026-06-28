from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Literal


class TransactionCreate(BaseModel):
    userId: str
    amount: float
    type: Literal["INCOME", "EXPENSE"]
    date: datetime
    month: str                    # SEMPRE EXISTE
    categoryId: Optional[str] = None
    description: Optional[str] = None

    # Parcelamento
    parentId: Optional[str] = None   # null = normal
    installmentIndex: Optional[int] = None
    totalInstallments: Optional[int] = None