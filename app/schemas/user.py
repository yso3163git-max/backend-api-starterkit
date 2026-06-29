from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
  name: str = Field(..., min_length=1, max_length=50)
  email: str = Field(..., min_length=5, max_length=100)


class UserResponse(BaseModel):
  id: int
  name: str
  email: str
