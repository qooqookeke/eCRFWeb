from datetime import datetime
from pydantic import BaseModel, Field, EmailStr, field_validator



class adminCreate(BaseModel):
    user_id : str
    hashed_pw : str
    username : str
    email : EmailStr
    phone : str

    class Config:
        from_attributes = True


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