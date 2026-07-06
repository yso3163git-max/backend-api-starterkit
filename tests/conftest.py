import pytest
from fastapi.testclient import TestClient

from main import app
from app.routers import users as users_router


@pytest.fixture
def client():
  users_router._users = [
    {"id": 1, "name": "홍길동", "email": "hong@example.com"},
    {"id": 2, "name": "김철수", "email": "kim@example.com"},
  ]
  users_router._next_id = 3
  return TestClient(app)
