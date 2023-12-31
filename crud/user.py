# app/crud/user.py
from sqlalchemy.orm import Session
from models.model_user import User
from schemas.user import UserCreate
from crud.base import CRUDBase

class CRUDUser(CRUDBase[User, UserCreate]):
    pass # All logic implemented in the base class

crud_user = CRUDUser(User, UserCreate)
