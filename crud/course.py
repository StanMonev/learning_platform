# app/crud/course.py
from sqlalchemy.orm import Session
from models.model_course import Course
from schemas.course import CourseCreate
from crud.base import CRUDBase

class CRUDCourse(CRUDBase[Course, CourseCreate]):
    pass # All logic implemented in the base class

crud_course = CRUDCourse(Course, CourseCreate)
