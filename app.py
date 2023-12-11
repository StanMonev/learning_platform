from fastapi import FastAPI
from models import user, lesson, course
from routes import router
from config.settings import engine

user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)
lesson.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router, prefix="/users", tags=["users"])
app.include_router(router, prefix="/courses", tags=["courses"])
app.include_router(router, prefix="/lessons", tags=["lessons"])