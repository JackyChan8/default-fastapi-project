from pydantic import BaseModel, EmailStr


class User(BaseModel):
    """
        Base Model Schema User
    """
    email: EmailStr
    password: str


class SignUp(User):
    """
        Model Schema SignUp
    """
    pass
