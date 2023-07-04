from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from helpers.deps import auth

from model import User
from . import schemas

router = APIRouter()


@router.get("/{user_id}", response_model=schemas.User)
def get_user(user_id: int) -> Any:
    """
    Get user by id

    Args:
        user_id: user id

    Returns:
        User
    """
    user = User.get_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=404, detail="User does not exist.",
        )
    return user


@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: int, user: User = Depends(auth)) -> Any:
    """
    Delete user
    An authenticated user can delete any other user

    Returns:
        Failure or 204
    """
    to_delete = User.get_by_id(user_id)
    if not to_delete:
        raise HTTPException(
            status_code=404, detail="User does not exist.",
        )
    print(user.email, " is deleting ", to_delete.email)
    to_delete.delete()
    return ""


@router.post("/", response_model=schemas.User)
def add_user(api_payload: schemas.UserCreate) -> Any:
    """
    Add new user

    Returns:
        User
    """
    user = User.get_by_email(api_payload.email)
    if user:
        raise HTTPException(
            status_code=400, detail="User already exists.",
        )
    user = User(**api_payload.dict()).insert()
    return user


@router.get("/", response_model=List[schemas.User])
def list_users() -> Any:
    """
    Get all users

    Returns:
        List of users
    """
    return User.list()
