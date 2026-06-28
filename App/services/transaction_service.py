from dateutil.relativedelta import relativedelta
from App.repositories.transaction_repo import (
    create_transaction_repo,
    delete_transaction,
    get_transaction_by_id,
    get_transactions_by_parent
)
from uuid import uuid4
from dateutil.relativedelta import relativedelta


def create_transaction(data):
    tx = data.dict()
    total = tx.get("totalInstallments", 1)
    base_date = tx["date"]

    # 🔹 Não parcelado
    if total == 1:
        tx["month"] = base_date.strftime("%Y-%m")
        tx["parentId"] = None
        tx["installmentIndex"] = None
        tx["totalInstallments"] = None
        return create_transaction_repo(tx)

    # 🔹 Parcelado
    parent_id = str(uuid4())  # 🔥 NÃO cria documento pai

    amount_per = round(tx["amount"] / total, 2)

    ids = []

    for i in range(total):
        due_date = base_date + relativedelta(months=i)

        installment = {
            **tx,
            "amount": amount_per,
            "month": due_date.strftime("%Y-%m"),
            "parentId": parent_id,
            "installmentIndex": i + 1,
            "totalInstallments": total,
        }

        ids.append(create_transaction_repo(installment))

    return ids

def resolve_root_id(tx: dict) -> str:
    return tx.get("parentTransactionId") or tx["id"]

def delete_transaction_service(tx_id: str):
    tx = get_transaction_by_id(tx_id)
    if not tx:
        return False

    parent_id = tx.get("parentId")
    # 🔹 Parcelada → deleta todas do grupo
    if parent_id:
        siblings = get_transactions_by_parent(parent_id)
        for s in siblings:
            
            delete_transaction(s["id"])
        return True

    # 🔹 Normal
    delete_transaction(tx_id)
    return True