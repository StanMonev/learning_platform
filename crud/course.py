# app/crud/course.py
from sqlalchemy.orm import Session
from models.course import Course
from schemas.course import CourseCreate
from crud.base import CRUDBase

class CRUDCourse(CRUDBase[Course, CourseCreate]):
    pass

crud_course = CRUDCourse(Course, CourseCreate)
