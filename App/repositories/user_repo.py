from App.core.firestore import db
from datetime import datetime

def create_user(user_id: str, data: dict):
    db.collection("users").document(user_id).set({
        **data,
        "createdAt": datetime.utcnow()
    })

def get_user(user_id: str):
    doc = db.collection("users").document(user_id).get()
    if not doc.exists:
        return None
    return doc.to_dict()