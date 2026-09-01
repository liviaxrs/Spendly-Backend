from fastapi import APIRouter, HTTPException, Depends
from App.models.user import UserCreate, UserUpdate, UserResponse
from App.services.user_service import sync_or_create_user, get_user_by_id, update_user_profile
from App.core.auth import get_current_user 

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/sync", status_code=201)
def create_or_sync_user(
    user_data: UserCreate = None, 
    current_user: dict = Depends(get_current_user)
):
    """
    O frontend chama esta rota logo após fazer o login no Firebase.
    Se for o primeiro acesso, salva no banco. Se não, apenas retorna os dados.
    """
    try:
        user = sync_or_create_user(current_user, user_data)
        return {"status": "success", "message": "Usuário criado perfeitamente"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/me")
def get_my_profile(current_user: dict = Depends(get_current_user)):
    """
    Busca o perfil de quem está fazendo a requisição. O UID vem do token, impossível fraudar.
    """
    try:
        return get_user_by_id(current_user["uid"])
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.patch("/me")
def update_my_profile(
    update_data: UserUpdate, 
    current_user: dict = Depends(get_current_user)
):
    try:
        return update_user_profile(current_user["uid"], update_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))