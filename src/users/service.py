from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.models import User
from .schema import userCreateModel
from sqlmodel import select

class userService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_user(self):
        statement = select(User).order_by(User.created_at)
        result = await self.session.exec(statement)
        return result.all()

    async def create_User(self, user_data: userCreateModel):
        new_user = User(**user_data.model_dump())
        self.session.add(new_user)  # Just use `self.session.add()` here, no need for `await`
        await self.session.commit()
        await self.session.refresh(new_user)  # Refresh the instance with the database state
        return new_user
