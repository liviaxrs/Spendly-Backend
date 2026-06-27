from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Literal


class TransactionCreate(BaseModel):
    userId: str
    amount: float
    type: Literal["INCOME", "EXPENSE"]
    date: datetime
    month: Optional[str] = None
    categoryId: Optional[str] = None
    description: Optional[str] = None

    # Installments
    totalInstallments: int = 1
    # INTERNAL USE ONLY
    installmentIndex: Optional[int] = Field(None, exclude=True)
    parentTransactionId: Optional[str] = Field(None, exclude=True)