from fastapi import APIRouter
from App.repositories.transaction_repo import get_month_transactions

router = APIRouter(prefix="/summary", tags=["Summary"])


@router.get("/{user_id}/{month}")
def monthly_summary(user_id: str, month: str):
    txs = get_month_transactions(user_id, month)

    income = sum(t["amount"] for t in txs if t["type"] == "INCOME")
    expenses = sum(t["amount"] for t in txs if t["type"] == "EXPENSE")

    return {
        "month": month,
        "income": income,
        "expenses": expenses,
        "balance": income - expenses
    }