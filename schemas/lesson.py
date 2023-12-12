from pydantic import BaseModel

class LessonCreate(BaseModel):
    title: str
    content: str
    course_id: int

class Lesson(LessonCreate):
    id: int

    class Config:
        orm_mode = True