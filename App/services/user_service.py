from App.repositories.user_repo import create_user, get_user
from App.models.user import UserCreate

def create_new_user(user_id: str, user: UserCreate):
    existing = get_user(user_id)
    if existing:
        raise ValueError("User already exists")

    create_user(user_id, user.dict())

def get_user_by_id(user_id: str):
    user = get_user(user_id)
    if not user:
        raise ValueError("User not found")
    return user