from datetime import datetime
from pydantic import BaseModel, Field, EmailStr, field_validator


class resultbase(BaseModel):
    id: int
    p_id: str
    visit: int
    code_id: str
    score: int
    created_at: datetime

    class Config:
        from_attributes = True

class resultCreate(resultbase):
    pass

class result_msg(BaseModel):
    msg: str