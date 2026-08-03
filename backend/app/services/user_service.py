from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate
from app.auth.password import hash_password

class UserService:
    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)

    # def __init__(self, user_repositories):
    #     self.user_repository = user_repositories

    def register_user(
        self,
        user_create: UserCreate
    ):

    # check if the email exist
        existing_user= self.user_repository.get_user_by_email(
            user_create.email
        )
        if existing_user:
            #Raise Exception
            return None


        hashed_password=hash_password(user_create.password)

        user=self.user_repository.create_user(
            user_data=user_create,
            hashed_password=hashed_password
        )
        return user


    # check Hash password

    # convert the pydantic to orm

    # save using the repository

    # return created user