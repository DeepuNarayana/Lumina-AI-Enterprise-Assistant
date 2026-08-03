from sqlalchemy.orm import Session

from app.repositories.user_repository import UserRepository

from app.auth.jwt_handler import create_access_token

from app.auth.password import verify_password

class AuthService:
    def __init__(self,db:Session):
        self.user_repository = UserRepository(db)

    def login(self, email:str, password:str):

        print(f"login email: {email}")

        user = self.user_repository.get_user_by_email(email)

        print("user found", user)

        # if user:
        #     print("Stored hash:",user.hashed_password)
        #     print("Password verified:", verify_password(password,user.hashed_password))

        if not user:
            return None

        #print("Stored hash", user.hashed_password)
        result = verify_password(
            password,
            user.hashed_password
        )
        print("password verified", result)

        if not verify_password(password, user.hashed_password):
            return None

        token = create_access_token(
            {
                "sub": user.email,
                "user_id": str(user.id)
            }
        )
        return token