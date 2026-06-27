from fastapi import APIRouter
from App.models.categories import CategoryCreate
from App.services.category_service import (
    create_new_category,
    list_user_categories,
    remove_category
)

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.post("/")
def create_category(category: CategoryCreate):
    category_id = create_new_category(category)
    return {"id": category_id, "message": "Category created"}


@router.get("/user/{user_id}")
def get_user_categories(user_id: str):
    return list_user_categories(user_id)


@router.delete("/{category_id}")
def delete_category(category_id: str):
    remove_category(category_id)
    return {"message": "Category deleted"}