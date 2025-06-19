# app/api/v1/endpoints/users.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def read_users():
    """
    Retrieve users.
    """
    return [{"username": "fakeuser"}]

@router.post("/")
async def create_user():
    """
    Create new user.
    """
    return {"message": "User created"}

@router.get("/{user_id}")
async def read_user(user_id: int):
    """
    Retrieve a specific user by ID.
    """
    return {"username": "fakeuser", "id": user_id}