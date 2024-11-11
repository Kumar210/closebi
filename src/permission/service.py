from fastapi import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.models import Permission
from .schema import Permission,permissionCreateModel
# from sqlmodel import select
from sqlalchemy.future import select
import bcrypt
from src.utils.jwt.jwt import create_jwt_token
from src.utils.bcrypt import verify_password


class permissionService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_user(self):
        statement = select(Permission).order_by(Permission.created_at)
        result = await self.session.exec(statement)
        return result.all()


    async def create_gcb(self, permission_data: permissionCreateModel):
        permission = Permission(**permission_data.model_dump())
        self.session.add(permission)  
        await self.session.commit()
        await self.session.refresh(permission)  
        return permission


