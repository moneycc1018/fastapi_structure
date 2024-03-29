from sqlalchemy.sql import select, insert
from app.user.models import User as UserModel
from app.user.schemas import CreateUserInput
from app.database import Session


def query_user(user_name):
    with Session() as session:
        stmt = select(UserModel).where(UserModel.name == user_name)
        result = session.scalars(stmt).one()

    return result


def create_user(user: CreateUserInput):
    with Session.begin() as session:
        stmt = insert(UserModel).values(**user.dict()).returning(UserModel)
        result = session.scalars(stmt).one()

    return result
