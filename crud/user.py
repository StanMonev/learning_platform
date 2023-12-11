# app/crud/user.py
from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate
from crud.base import CRUDBase

class CRUDUser(CRUDBase[User, UserCreate]):
    pass

crud_user = CRUDUser(User, UserCreate)
