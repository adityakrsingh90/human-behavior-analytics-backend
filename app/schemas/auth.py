from pydantic import BaseModel, EmailStr

class LoginSchema(BaseModel):
    email: EmailStr
    password: str

class SignupSchema(BaseModel):
    email: EmailStr
    password: str
