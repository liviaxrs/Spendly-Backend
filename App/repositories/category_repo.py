from App.core.firestore import db


# CREATE
def create_category(data: dict):
    ref = db.collection("categories").document()
    ref.set(data)
    return ref.id


# GET BY USER
def get_categories_by_user(user_id: str):
    docs = db.collection("categories").where("userId", "==", user_id).stream()
    return [{"id": d.id, **d.to_dict()} for d in docs]


# DELETE
def delete_category(category_id: str):
    db.collection("categories").document(category_id).delete()