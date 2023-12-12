# app/crud/lesson.py
from sqlalchemy.orm import Session
from models.model_lesson import Lesson
from schemas.lesson import LessonCreate
from crud.base import CRUDBase

class CRUDLesson(CRUDBase[Lesson, LessonCreate]):
    pass # All logic implemented in the base class

crud_lesson = CRUDLesson(Lesson, LessonCreate)
