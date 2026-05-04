from datetime import datetime
from pydantic import BaseModel, ConfigDict
from typing import List, Optional,Dict


class create_user(BaseModel):
    name: str
    username: str
    email: str
    password: str
    phone: Optional[str] = None
    type: Optional[str] = None

class response_user(BaseModel):
    id: int
    name: str
    username: str
    email: str
    phone: str
    type: str
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class update_user(BaseModel):
    name: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    phone: Optional[str] = None
    type: Optional[str] = None