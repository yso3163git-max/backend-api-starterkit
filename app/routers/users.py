from fastapi import APIRouter

from app.exceptions import NotFoundError, BadRequestError
from app.schemas.common import SuccessResponse
from app.schemas.user import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["users"])

# 인메모리 더미 데이터
_users: list[dict] = [
  {"id": 1, "name": "홍길동", "email": "hong@example.com"},
  {"id": 2, "name": "김철수", "email": "kim@example.com"},
]
_next_id = 3


@router.get("", response_model=SuccessResponse)
async def list_users():
  return SuccessResponse(data=_users)


@router.get("/{user_id}", response_model=SuccessResponse)
async def get_user(user_id: int):
  user = next((u for u in _users if u["id"] == user_id), None)
  if not user:
    raise NotFoundError(f"ID {user_id}인 유저를 찾을 수 없습니다.")
  return SuccessResponse(data=user)


@router.post("", response_model=SuccessResponse, status_code=201)
async def create_user(body: UserCreate):
  global _next_id
  if any(u["email"] == body.email for u in _users):
    raise BadRequestError(f"이미 사용 중인 이메일입니다: {body.email}")
  new_user = {"id": _next_id, "name": body.name, "email": body.email}
  _users.append(new_user)
  _next_id += 1
  return SuccessResponse(data=new_user)


@router.delete("/{user_id}", response_model=SuccessResponse)
async def delete_user(user_id: int):
  user = next((u for u in _users if u["id"] == user_id), None)
  if not user:
    raise NotFoundError(f"ID {user_id}인 유저를 찾을 수 없습니다.")
  _users.remove(user)
  return SuccessResponse(data={"deleted_id": user_id})
