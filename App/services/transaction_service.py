from dateutil.relativedelta import relativedelta
from App.repositories.transaction_repo import (
    create_transaction_repo,
    delete_transaction,
    get_transaction_by_id,
    get_transactions_by_parent
)

def create_transaction(data):
    tx = data.dict(exclude_none=True)
    base_date = tx["date"]
    total = tx.get("totalInstallments", 1)

    # Single transaction
    if total <= 1:
        tx["month"] = base_date.strftime("%Y-%m")
        return create_transaction_repo(tx)

    # Parent transaction (group only)
    parent_tx = {
        **tx,
        "month": base_date.strftime("%Y-%m")
    }

    parent_id = create_transaction_repo(parent_tx)

    amount_per = tx["amount"] / total

    for i in range(total):
        due_date = base_date + relativedelta(months=i)

        installment_tx = {
            **tx,
            "amount": round(amount_per, 2),
            "month": due_date.strftime("%Y-%m"),
            "installmentIndex": i + 1,
            "parentTransactionId": parent_id
        }

        create_transaction_repo(installment_tx)

    return parent_id

def resolve_root_id(tx: dict) -> str:
    return tx.get("parentTransactionId") or tx["id"]

def delete_transaction_service(tx_id: str):
    tx = get_transaction_by_id(tx_id)

    if not tx:
        return False

    root_id = resolve_root_id(tx)

    # delete children
    children = get_transactions_by_parent(root_id)
    print(children)
    for c in children:
        delete_transaction(c["id"])

    # delete root (parent or single transaction)
    delete_transaction(root_id)

    return True