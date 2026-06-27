from fastapi import APIRouter, HTTPException
from App.models.user import UserCreate
from App.services.user_service import create_new_user, get_user_by_id

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/{user_id}", status_code=201)
def create_user(user_id: str, user: UserCreate):
    try:
        create_new_user(user_id, user)
        return {"message": "User created"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{user_id}")
def get_user(user_id: str):
    try:
        return get_user_by_id(user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))