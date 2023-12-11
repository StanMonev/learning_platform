from pydantic import BaseModel

class CourseCreate(BaseModel):
    name: str
    description: str

class Course(CourseCreate):
    id: int

    class Config:
        orm_mode = True