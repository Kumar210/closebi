from fastapi import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.models import User
from .schema import userCreateModel,login
# from sqlmodel import select
from sqlalchemy.future import select
import bcrypt
from src.utils.jwt.jwt import create_jwt_token
from src.utils.bcrypt import verify_password



class userService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_user(self):
        statement = select(User).order_by(User.created_at)
        result = await self.session.exec(statement)
        return result.all()

    async def create_User(self, user_data: userCreateModel):
    # Check if user already exists
        statement = select(User).where(User.email == user_data.email)
        result = await self.session.exec(statement)
        existing_user = result.scalar_one_or_none()
    
        if existing_user:
            raise HTTPException(status_code=400, detail="User with this email already exists")

    # Hash the password and convert to string
        hashed_password = bcrypt.hashpw(user_data.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')  # decode bytes to string

    # Use model_dump to get the data and update the password
        user_dict = user_data.model_dump() 
        user_dict['password'] = hashed_password

    # Create a new user with the hashed password
        new_user = User(**user_dict)

        self.session.add(new_user)
        await self.session.commit()
        await self.session.refresh(new_user)

        return new_user
    
    
    async def login(self,userLogin:login,secret_key: str):
        statement = select(User).where(User.email == userLogin.email)
        result = await self.session.exec(statement)
        existing_user = result.scalar_one_or_none()
    
    # Check the Email Id 
        if not existing_user:
            raise HTTPException(status_code=400, detail="Email Not Found")
        
    # verify the password
        if not verify_password(userLogin.password, existing_user.password):
            raise HTTPException(status_code=400, detail="Incorrect password")

        token = create_jwt_token(existing_user.id, existing_user.email, secret_key)
        return {"user": existing_user, "token": token}