from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from typing import Optional

class UserRepository():

    def __init__(self, db:Session):
        self.db=db

    def create_user(
        self,
        user_data:UserCreate,
        hashed_password: str
    )->User:

        user=User(
            full_name= user_data.full_name,
            email=user_data.email,
            hashed_password=hashed_password
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user

    def get_user_by_email(self, email:str)->User | None:
        user=self.db.query(User).filter(User.email==email).one_or_none()
        return user
        #self.filter(User.email=='email')
        #self.one_or_none()
