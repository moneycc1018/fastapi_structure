from pydantic import BaseModel


class QueryUserInput(BaseModel):
    name: str


class QueryUserResponse(BaseModel):
    name: str
    age: int
    subscription: str

    class Config:
        orm_mode = True


class CreateUserInput(BaseModel):
    name: str
    age: int
