from fastapi import APIRouter
from app.user import service
from app.user.schemas import QueryUserInput, QueryUserResponse, CreateUserInput

router = APIRouter()


@router.post("/", response_model=QueryUserResponse)
async def get_user(input: QueryUserInput):
    user = service.query_user(input.name)

    return user


@router.post("/new-user")
async def add_user(input: CreateUserInput):
    user = service.create_user(input)

    return user
