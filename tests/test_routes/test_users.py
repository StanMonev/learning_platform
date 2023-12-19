import json
import fakeredis
from unittest.mock import patch
from unittest.mock import MagicMock
from config.settings import Settings

#Not fully functional Works if Redis is on. Must implement a Mock Redis connection.

#@patch("redis.asyncio", return_value=fakeredis.FakeStrictRedis())
def test_create_user(client):
    data = {"username":"testuser","email":"testuser@nofoobar.com","password":"testing"}
    response = client.post("/users", json=data)
    assert response.status_code == 200 
    assert response.json()["email"] == "testuser@nofoobar.com"

def test_get_user(client):
    response = client.get("/users")
    assert response.status_code == 200