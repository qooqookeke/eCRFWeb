from datetime import datetime
from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import List, Optional


class infoBase(BaseModel):
    initial: str
    p_id: str
    birth: str
    sex: int
    weight: float
    height: float
    site: int
    op: int
    hx: str
    smoke: int
    alcohol: int
    exercise: int

    class Config:
        from_attributes = True

# 환자 정보 생성
class infoBaseCreate(infoBase):

    @field_validator('p_id')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('환자 번호를 입력해주세요.')
        return v

# 리스트 결과
class PInfoResponse(BaseModel):
    data: List[infoBase]
    count: int


# 환자 정보 변경
class infoBaseUpdate(infoBase):
    pass

# 환자 정보 삭제
class infoBaseDelete(infoBase):
    pass