from datetime import datetime
from pydantic import BaseModel, Field, EmailStr, field_validator

class infoBase(BaseModel):
    id: int
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
    created_at: datetime

    class Config:
        from_attributes = True

class infoBaseCreate(infoBase):
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

    @field_validator('p_id')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v


class infoBaseUpdate(infoBaseCreate):
    pass

class infoBaseDelete(infoBase):
    id: int


class sv_womac(BaseModel):
    code_id: str
    first_code: str
    middle_code: str
    last_code: str
    description: str

    class Config:
        from_attributes = True

class sv_koos(BaseModel):
    code_id: str
    first_code: str
    middle_code: str
    last_code: str
    description: str

    class Config:
        from_attributes = True

class sv_ikdc(BaseModel):
    code_id: str
    first_code: str
    middle_code: str
    last_code: str
    description: str

    class Config:
        from_attributes = True


class sv_ls(BaseModel):
    code_id: str
    first_code: str
    middle_code: str
    last_code: str
    description: str

    class Config:
        from_attributes = True

class sv_etc(BaseModel):
    code_id: str
    first_code: str
    middle_code: str
    last_code: str
    description: str

    class Config:
        from_attributes = True


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



# class UsersCreateItem(BaseModel):
#     user_id: str = Field(
#         default=None, title='사용자 아이디'
#     )
#     email: EmailStr = Field(
#         default=None, title='이메일 형식의 아이디'
#     )
#     password: str = Field(
#         min_length=8, max_length=20, description='비밀번호는 8~20자의 영문, 숫자, 특수문자 조합으로 작성해주세요.'
#     )
#     nickname: str = Field(
#         min_length=2, max_length=8, description='닉네임은 2~8글자의 영문 또는 한글로 만들어주세요.'
#     )

#     class Config:
#         from_attributes = True

# class UsersUpdateItem(BaseModel):
#     email: EmailStr | None
#     nickname: str | None

#     class Config:
#         from_attributes = True

# class UsersReadItem(BaseModel):
#     email: EmailStr
#     user_id: str
#     nickname: str

#     class Config:
#         from_attributes = True