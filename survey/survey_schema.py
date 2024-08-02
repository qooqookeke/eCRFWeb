from pydantic import BaseModel, Field, EmailStr, field_validator


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
