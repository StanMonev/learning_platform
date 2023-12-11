# tests/test_crud.py
from sqlalchemy.orm import Session
from fastapi.testclient import TestClient
from config.settings import get_settings, override_settings
from app import app
from config.settings import SessionLocal, engine
from models.user import User
from crud.user import CRUDUser
from schemas.user import UserCreate

# Apply database migrations
from alembic import command
from alembic.config import Config

alembic_cfg = Config("alembic.ini")
command.upgrade(alembic_cfg, "head")

# Override settings to use a test database
settings = get_settings()
test_settings = override_settings(settings, test=True)
app.dependency_overrides[get_settings] = lambda: test_settings

# Create a test database session
def override_get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[Session] = override_get_db

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
