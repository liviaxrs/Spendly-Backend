from App.core.firestore import db


def create_transaction_repo(data: dict):
    ref = db.collection("transactions").document()
    ref.set(data)
    return ref.id

def get_month_transactions(user_id: str, month: str):
    docs = db.collection("transactions") \
        .where("userId", "==", user_id) \
        .where("month", "==", month) \
        .stream()

    return [{"id": d.id, **d.to_dict()} for d in docs]

def delete_transaction(tx_id: str):
    db.collection("transactions").document(tx_id).delete()


def get_transaction_by_id(tx_id: str):
    doc = db.collection("transactions").document(tx_id).get()
    return doc.to_dict() if doc.exists else None


def get_transactions_by_parent(parent_id: str):
    docs = db.collection("transactions") \
        .where("parentId", "==", parent_id) \
        .stream()

    return [{"id": d.id, **d.to_dict()} for d in docs]