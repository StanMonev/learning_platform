# app/crud/base.py
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import DeclarativeMeta
from pydantic import BaseModel
from typing import TypeVar, Generic, List

ModelType = TypeVar("ModelType", bound=DeclarativeMeta)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)

class CRUDBase(Generic[ModelType, CreateSchemaType]):
    def __init__(self, model: ModelType, schema: CreateSchemaType):
        self.model = model
        self.schema = schema

    def create(self, db: Session, obj_in: CreateSchemaType) -> ModelType:
        db_obj = self.model(**obj_in.__dict__)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def get_all(self, db: Session, limit: int = 100) -> List[ModelType]:
        return db.query(self.model).limit(limit).all()

    def read(self, db: Session, obj_id: int) -> ModelType:
        return db.query(self.model).filter(self.model.id == obj_id).first()

    def update(self, db: Session, obj_id: int, obj_in: CreateSchemaType) -> ModelType:
        db_obj = db.query(self.model).filter(self.model.id == obj_id).first()
        if db_obj:
            for key, value in obj_in.__dict__.items():
                setattr(db_obj, key, value)
            db.commit()
            db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, obj_id: int) -> ModelType:
        obj = db.query(self.model).filter(self.model.id == obj_id).first()
        if obj:
            db.delete(obj)
            db.commit()
        return obj
