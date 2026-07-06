USERS_URL = "/api/v1/users"


def test_list_users(client):
  response = client.get(USERS_URL)

  assert response.status_code == 200
  assert len(response.json()["data"]) == 2


def test_get_user_found(client):
  response = client.get(f"{USERS_URL}/1")

  assert response.status_code == 200
  assert response.json()["data"]["email"] == "hong@example.com"


def test_get_user_not_found(client):
  response = client.get(f"{USERS_URL}/999")

  assert response.status_code == 404
  assert response.json()["error"]["code"] == "NOT_FOUND"


def test_create_user_success(client):
  response = client.post(USERS_URL, json={"name": "이영희", "email": "lee@example.com"})

  assert response.status_code == 201
  assert response.json()["data"]["email"] == "lee@example.com"


def test_create_user_duplicate_email(client):
  response = client.post(USERS_URL, json={"name": "홍길동2", "email": "hong@example.com"})

  assert response.status_code == 400
  assert response.json()["error"]["code"] == "BAD_REQUEST"


def test_create_user_invalid_email(client):
  response = client.post(USERS_URL, json={"name": "이영희", "email": "not-an-email"})

  assert response.status_code == 422
  assert response.json()["error"]["code"] == "VALIDATION_ERROR"


def test_delete_user_found(client):
  response = client.delete(f"{USERS_URL}/1")

  assert response.status_code == 200
  assert response.json()["data"]["deleted_id"] == 1


def test_delete_user_not_found(client):
  response = client.delete(f"{USERS_URL}/999")

  assert response.status_code == 404
  assert response.json()["error"]["code"] == "NOT_FOUND"
