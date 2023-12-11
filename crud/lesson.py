# app/crud/lesson.py
from sqlalchemy.orm import Session
from models.lesson import Lesson
from schemas.lesson import LessonCreate
from crud.base import CRUDBase

class CRUDLesson(CRUDBase[Lesson, LessonCreate]):
    pass

crud_lesson = CRUDLesson(Lesson, LessonCreate)
