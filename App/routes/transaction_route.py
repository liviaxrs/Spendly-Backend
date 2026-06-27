from fastapi import APIRouter, HTTPException
from App.models.transaction import TransactionCreate
from App.services.transaction_service import create_transaction, delete_transaction_service
from App.repositories.transaction_repo import get_month_transactions


router = APIRouter(prefix="/transactions", tags=["Transactions"])


@router.post("/")
def create(tx: TransactionCreate):
    tx_id = create_transaction(tx)
    return {"id": tx_id}


@router.get("/month/{user_id}/{month}")
def by_month(user_id: str, month: str):
    return get_month_transactions(user_id, month)


@router.delete("/{transaction_id}")
def delete_transaction(transaction_id: str):
    success = delete_transaction_service(transaction_id)

    if not success:
        raise HTTPException(status_code=404, detail="Transaction not found")

    return {"message": "Transaction deleted successfully"}