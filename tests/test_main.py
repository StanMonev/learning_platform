# tests/test_main.py

from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"username": "testuser", "email": "test@example.com", "password": "testpass"})
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"
    assert response.json()["email"] == "test@example.com"

def test_read_user():
    response_create = client.post("/users/", json={"username": "testuser", "email": "test@example.com", "password": "testpass"})
    user_id = response_create.json()["id"]

    response_read = client.get(f"/users/{user_id}")
    assert response_read.status_code == 200
    assert response_read.json()["username"] == "testuser"
    assert response_read.json()["email"] == "test@example.com"

def test_create_course():
    response = client.post("/courses/", json={"name": "Test Course", "description": "This is a test course"})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Course"
    assert response.json()["description"] == "This is a test course"

def test_read_course():
    response_create = client.post("/courses/", json={"name": "Test Course", "description": "This is a test course"})
    course_id = response_create.json()["id"]

    response_read = client.get(f"/courses/{course_id}")
    assert response_read.status_code == 200
    assert response_read.json()["name"] == "Test Course"
    assert response_read.json()["description"] == "This is a test course"

def test_create_lesson():
    response_create_course = client.post("/courses/", json={"name": "Test Course", "description": "This is a test course"})
    course_id = response_create_course.json()["id"]

    response_create_lesson = client.post("/lessons/", json={"title": "Test Lesson", "content": "This is a test lesson", "course_id": course_id})
    assert response_create_lesson.status_code == 200
    assert response_create_lesson.json()["title"] == "Test Lesson"
    assert response_create_lesson.json()["content"] == "This is a test lesson"
    assert response_create_lesson.json()["course_id"] == course_id

def test_read_lesson():
    response_create_course = client.post("/courses/", json={"name": "Test Course", "description": "This is a test course"})
    course_id = response_create_course.json()["id"]

    response_create_lesson = client.post("/lessons/", json={"title": "Test Lesson", "content": "This is a test lesson", "course_id": course_id})
    lesson_id = response_create_lesson.json()["id"]

    response_read_lesson = client.get(f"/lessons/{lesson_id}")
    assert response_read_lesson.status_code == 200
    assert response_read_lesson.json()["title"] == "Test Lesson"
    assert response_read_lesson.json()["content"] == "This is a test lesson"
    assert response_read_lesson.json()["course_id"] == course_id
