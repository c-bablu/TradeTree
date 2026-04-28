from datetime import datetime
from typing import Any
from pydantic import BaseModel, ConfigDict

class success_response(BaseModel):
    data: Any
    message: str
    status: str

class error_response(BaseModel):
    data: list = []
    message: str
    status: str