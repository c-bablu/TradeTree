from datetime import datetime
from pydantic import BaseModel, ConfigDict



class create_user(BaseModel):
    name: str
    username: str
    email: str
    password: str
    phone: str
    type: str

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

