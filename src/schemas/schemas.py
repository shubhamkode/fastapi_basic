import pydantic as _pydantic

class _UserBase(_pydantic.BaseModel):
    name: str
    email: _pydantic.EmailStr

class UserCreate(_UserBase):
    password: str

class User(_UserBase):
    id: int
    class Config:
        orm_mode=True
