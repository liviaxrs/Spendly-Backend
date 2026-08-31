from App.repositories.user_repo import create_user, get_user, update_user
from App.models.user import UserCreate, UserUpdate

def sync_or_create_user(auth_token_data: dict, additional_data: UserCreate = None):
    """
    Sincroniza o usuário do Firebase Auth com o Firestore.
    auth_token_data é o dicionário que vem do get_current_user (nosso validador de token).
    """
    user_id = auth_token_data["uid"]
    existing_user = get_user(user_id)
    
    if existing_user:
        return existing_user
    new_user_data = {
        "email": auth_token_data.get("email"),
        "name": additional_data.name if additional_data else auth_token_data.get("name", "Usuário"),
        "photoUrl": auth_token_data.get("picture"), # Vem preenchido se logar com Google
        "role": "user",
        "isActive": True
    }
    
    return create_user(user_id, new_user_data)

def get_user_by_id(user_id: str):
    user = get_user(user_id)
    if not user:
        raise ValueError("User not found")
    return user
    
def update_user_profile(user_id: str, update_data: UserUpdate):
    clean_data = {k: v for k, v in update_data.dict().items() if v is not None}
    if clean_data:
        update_user(user_id, clean_data)
    
    return get_user_by_id(user_id)