from App.core.firestore import db
from google.cloud import firestore

def create_user(user_id: str, data: dict):
    data["createdAt"] = firestore.SERVER_TIMESTAMP
    data["updatedAt"] = firestore.SERVER_TIMESTAMP
    db.collection("users").document(user_id).set(data)
    return {**data, "id": user_id}

def get_user(user_id: str):
    doc = db.collection("users").document(user_id).get()
    if not doc.exists:
        return None
    
    user_data = doc.to_dict()
    user_data["id"] = doc.id
    return user_data

def update_user(user_id: str, data: dict):
    data["updatedAt"] = firestore.SERVER_TIMESTAMP
    db.collection("users").document(user_id).update(data)