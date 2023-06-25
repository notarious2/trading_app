from fastapi_users import schemas
from datetime import datetime

class UserRead(schemas.BaseUser[int]):
    pass


class UserCreate(schemas.BaseUserCreate):
    id: int
    username: str
    role_id: int


class UserUpdate(schemas.BaseUserUpdate):
    id: int
    username: str
    role_id: int