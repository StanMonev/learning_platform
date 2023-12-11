# app/routes.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.user import UserCreate, User
from schemas.course import CourseCreate, Course
from schemas.lesson import LessonCreate, Lesson
from config.settings import get_limiter
from config.settings import get_cache
from crud.user import crud_user
from crud.course import crud_course
from crud.lesson import crud_lesson
from config.settings import SessionLocal

#Router
router = APIRouter()

#Limiter
limiter = get_limiter()

# Cache configuration
cache = get_cache()
cache_time = 60  # Cache for 60 seconds

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

##############################################USERS#####################################################

#Get All Users with a default limit of 100
@router.get("/users")
async def get_all_users(db: Session = Depends(get_db)):
    users = crud_user.get_all(db)
    return users

#Get user by id
@router.get("/users/{user_id}")
async def read_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    user = crud_user.read_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

#Update user by id
@router.put("/users/{user_id}")
async def update_user_endpoint(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    updated_user = crud_user.update_user(db, user_id, user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

#Delete user by id
@router.delete("/users/{user_id}")
async def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    deleted_user = crud_user.delete_user(db, user_id)
    if deleted_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return deleted_user

##########################################COURSES#####################################################

#Get All Courses with a default limit of 100
@router.get("/courses")
async def get_all_courses(db: Session = Depends(get_db)):
    courses = crud_course.get_all(db)
    return courses

#Get course by id
@router.get("/courses/{course_id}")
async def read_course_endpoint(course_id: int, db: Session = Depends(get_db)):
    course = crud_course.read_course(db, course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

#Update course by id
@router.put("/courses/{course_id}")
async def update_course_endpoint(course_id: int, course: CourseCreate, db: Session = Depends(get_db)):
    updated_course = crud_course.update_course(db, course_id, course)
    if updated_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return updated_course

#Update course by id
@router.delete("/courses/{course_id}")
async def delete_course_endpoint(course_id: int, db: Session = Depends(get_db)):
    deleted_course = crud_course.delete_course(db, course_id)
    if deleted_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return deleted_course

##########################################LESSONS#####################################################

#Get All Lessons with a default limit of 100
@router.get("/lessons")
async def get_all_users(db: Session = Depends(get_db)):
    lesson = crud_lesson.get_all(db)
    return lesson

#Get lesson by id
@router.get("/lessons/{lesson_id}")
async def read_lesson_endpoint(lesson_id: int, db: Session = Depends(get_db)):
    lesson = crud_lesson.read(db, lesson_id)
    if lesson is None:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return lesson

#Update lesson by id
@router.put("/lessons/{lesson_id}")
async def update_lesson_endpoint(lesson_id: int, lesson: LessonCreate, db: Session = Depends(get_db)):
    updated_lesson = crud_lesson.update(db, lesson_id, lesson)
    if updated_lesson is None:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return updated_lesson

#Delete lesson by id
@router.delete("/lessons/{lesson_id}")
async def delete_lesson_endpoint(lesson_id: int, db: Session = Depends(get_db)):
    deleted_lesson = crud_lesson.delete(db, lesson_id)
    if deleted_lesson is None:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return deleted_lesson
