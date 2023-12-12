from fastapi import FastAPI
from models import model_user, model_course, model_lesson
from routes import router
from config.settings import engine
from loguru import logger

logger.add("logs/app.log", rotation="500 MB", level="INFO")

model_user.Base.metadata.create_all(bind=engine)
model_course.Base.metadata.create_all(bind=engine)
model_lesson.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router, prefix="/routes", tags=["Routes"])