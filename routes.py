# app/routes.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.user import UserCreate, User
from schemas.course import CourseCreate, Course
from schemas.lesson import LessonCreate, Lesson
from crud.user import crud_user
from crud.course import crud_course
from crud.lesson import crud_lesson
from config.settings import SessionLocal
from config.settings import Settings
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
from fastapi_cache import FastAPICache
from fastapi_cache.decorator import cache
from loguru import logger

#Router
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@cache()
async def get_cache():
    return 1


@router.on_event("startup")
async def startup():
    settings = Settings()
    redis = settings.get_redis()
    FastAPICache.init(redis, prefix="fastapi-cache")
    await FastAPILimiter.init(redis)
##############################################USERS#####################################################

#Get All Users with a default limit of 100
@router.get("/users", dependencies=[Depends(RateLimiter(times=2, seconds=5))])
async def get_all_users(db: Session = Depends(get_db)):
    logger.info(f"Fetching users...")
    users = crud_user.get_all(db)
    return users

#Get user by id
@router.get("/users/{user_id}", dependencies=[Depends(RateLimiter(times=2, seconds=5))])
@cache(expire=60)
async def read_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    user = crud_user.read(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    logger.info(f"Fetching user: {user.username}")
    return user

@router.post("/users", dependencies=[Depends(RateLimiter(times=2, seconds=5))])
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    logger.info(f"Creating user: {user.username}")
    return crud_user.create(db, user)

#Update user by id
@router.put("/users/{user_id}", dependencies=[Depends(RateLimiter(times=2, seconds=5))])
@cache(expire=60)
async def update_user_endpoint(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    logger.info(f"Updating user: {user.username}")
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    updated_user = crud_user.update(db, user_id, user)
    return updated_user

#Delete user by id
@router.delete("/users/{user_id}", dependencies=[Depends(RateLimiter(times=2, seconds=5))])
@cache(expire=60)
async def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    deleted_user = crud_user.delete(db, user_id)
    if deleted_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    logger.info(f"Deleting user: {deleted_user.username}")
    return deleted_user

##########################################COURSES#####################################################

#Get All Courses with a default limit of 100
@router.get("/courses", dependencies=[Depends(RateLimiter(times=2, seconds=5))])
async def get_all_courses(db: Session = Depends(get_db)):
    logger.info(f"Fetching courses...")
    courses = crud_course.get_all(db)
    return courses

#Get course by id
@router.get("/courses/{course_id}", dependencies=[Depends(RateLimiter(times=2, seconds=5))])
@cache(expire=60)
async def read_course_endpoint(course_id: int, db: Session = Depends(get_db)):
    course = crud_course.read(db, course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    logger.info(f"Fetching course: {course.name}")
    return course

@router.post("/courses", dependencies=[Depends(RateLimiter(times=2, seconds=5))])
async def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    logger.info(f"Creating course: {course.name}")
    return crud_course.create(db, course)

#Update course by id
@router.put("/courses/{course_id}", dependencies=[Depends(RateLimiter(times=2, seconds=5))])
@cache(expire=60)
async def update_course_endpoint(course_id: int, course: CourseCreate, db: Session = Depends(get_db)):
    updated_course = crud_course.update(db, course_id, course)
    if updated_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    logger.info(f"Updated course: {updated_course.name}")
    return updated_course

#Update course by id
@router.delete("/courses/{course_id}", dependencies=[Depends(RateLimiter(times=2, seconds=5))])
@cache(expire=60)
async def delete_course_endpoint(course_id: int, db: Session = Depends(get_db)):
    deleted_course = crud_course.delete(db, course_id)
    if deleted_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    logger.info(f"Deleted course: {deleted_course.name}")
    return deleted_course

##########################################LESSONS#####################################################

#Get All Lessons with a default limit of 100
@router.get("/lessons", dependencies=[Depends(RateLimiter(times=2, seconds=5))])
async def get_all_lessons(db: Session = Depends(get_db)):
    logger.info(f"Fetching lessons...")
    lesson = crud_lesson.get_all(db)
    return lesson

#Get lesson by id
@router.get("/lessons/{lesson_id}", dependencies=[Depends(RateLimiter(times=2, seconds=5))])
@cache(expire=60)
async def read_lesson_endpoint(lesson_id: int, db: Session = Depends(get_db)):
    lesson = crud_lesson.read(db, lesson_id)
    if lesson is None:
        raise HTTPException(status_code=404, detail="Lesson not found")
    logger.info(f"Fetching lesson: {lesson.title}")
    return lesson

@router.post("/lessons", dependencies=[Depends(RateLimiter(times=2, seconds=5))])
async def create_lesson(lesson: LessonCreate, db: Session = Depends(get_db)):
    logger.info(f"Creating lesson: {lesson.title}")
    return crud_lesson.create(db, lesson)

#Update lesson by id
@router.put("/lessons/{lesson_id}", dependencies=[Depends(RateLimiter(times=2, seconds=5))])
@cache(expire=60)
async def update_lesson_endpoint(lesson_id: int, lesson: LessonCreate, db: Session = Depends(get_db)):
    updated_lesson = crud_lesson.update(db, lesson_id, lesson)
    if updated_lesson is None:
        raise HTTPException(status_code=404, detail="Lesson not found")
    logger.info(f"Updated lesson: {updated_lesson.title}")
    return updated_lesson

#Delete lesson by id
@router.delete("/lessons/{lesson_id}", dependencies=[Depends(RateLimiter(times=2, seconds=5))])
@cache(expire=60)
async def delete_lesson_endpoint(lesson_id: int, db: Session = Depends(get_db)):
    deleted_lesson = crud_lesson.delete(db, lesson_id)
    if deleted_lesson is None:
        raise HTTPException(status_code=404, detail="Lesson not found")
    logger.info(f"Deleted lesson: {deleted_lesson.title}")
    return deleted_lesson
