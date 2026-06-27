from App.repositories.category_repo import (
    create_category,
    get_categories_by_user,
    delete_category
)


def create_new_category(category_data):
    return create_category(category_data.dict())


def list_user_categories(user_id: str):
    return get_categories_by_user(user_id)


def remove_category(category_id: str):
    delete_category(category_id)