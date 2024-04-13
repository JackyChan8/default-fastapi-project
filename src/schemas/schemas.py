from pydantic import BaseModel


class TestCreate(BaseModel):
    text: str
    is_test: bool
