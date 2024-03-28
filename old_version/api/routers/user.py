from fastapi import APIRouter, Depends
from api.dependencies import get_db
from sqlalchemy.orm import Session
import crud.user as crud
from schemas.user import QueryUserInput, QueryUserResponse, CreateUserInput

router = APIRouter()


@router.post("/", response_model=QueryUserResponse)
async def get_user(input: QueryUserInput, db: Session = Depends(get_db)):
    user = crud.query_user(db, input.name)

    return user


@router.post("/new-user")
async def add_user(input: CreateUserInput, db: Session = Depends(get_db)):
    user = crud.create_user(db, input)

    return user
