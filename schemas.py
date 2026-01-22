from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreate(BaseModel):
    company_name: str
    name: str
    email: EmailStr
    address: str
    password: str

class UserResponse(BaseModel):
    id: int
    company_name: str
    name: str
    email: str

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse