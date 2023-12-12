""" # tests/test_crud.py
import os
from sqlalchemy.orm import Session
from fastapi.testclient import TestClient
from config.settings import Settings, SessionLocal, engine, get_redis
from app import app
from routes import router
from config.settings import SessionLocal, engine
from models.model_user import User
from crud.user import CRUDUser
from schemas.user import UserCreate

# Load environment variables from .env.test
from dotenv import load_dotenv

load_dotenv('.env.test')

# Apply database migrations
from alembic import command
from alembic.config import Config

alembic_cfg = Config("alembic.ini")
command.upgrade(alembic_cfg, "head")

# Override settings to use a test database
settings = Settings()
test_settings = Settings(
    database_url=os.getenv('DATABASE_URL'),
    redis_url=os.getenv('REDIS_URL')
)

# Create a test database session
def override_get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[Session] = override_get_db
app.include_router(router, prefix="/routes", tags=["Routes"])

# Create a test client
client = TestClient(app)

def test_create_user():
    # Test creating a user
    response = client.post("/users/", json={"username": "testuser", "email": "test@example.com"})
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "testuser"
    assert data["email"] == "test@example.com"

def test_read_user():
    # Test reading a user
    user_id = 1  # Assuming the ID of the created user is 1
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id

def test_get_all_users():
    # Test getting all users
    response = client.get("/users/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

def test_update_user():
    # Test updating a user
    user_id = 1  # Assuming the ID of the created user is 1
    response = client.put(f"/users/{user_id}", json={"username": "updateduser"})
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "updateduser"

def test_delete_user():
    # Test deleting a user
    user_id = 1  # Assuming the ID of the created user is 1
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id
 """