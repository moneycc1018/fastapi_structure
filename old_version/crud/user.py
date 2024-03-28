from sqlalchemy.orm import Session
from models.user import User as UserModel
from schemas.user import CreateUserInput


def query_user(db: Session, user_name):
    return db.query(UserModel).where(UserModel.name == user_name).one()


def create_user(db: Session, user: CreateUserInput):
    db_user = UserModel(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user
