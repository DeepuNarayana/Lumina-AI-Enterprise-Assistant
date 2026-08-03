from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, EmailStr, ConfigDict

class UserCreate(BaseModel):
    full_name:str
    email: EmailStr
    password:str

class UserResponse(BaseModel):
    id:UUID
    full_name:str
    email:EmailStr
    is_active:bool
    created_at:datetime

    model_config=ConfigDict(from_attributes=True)