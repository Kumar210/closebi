from fastapi import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.models import Role
from .schema import Role,roleCreateModel
from sqlalchemy.future import select


class roleService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_user(self):
        statement = select(Role).order_by(Role.created_at)
        result = await self.session.exec(statement)
        return result.all()
    

    async def createRole(self, roleData: roleCreateModel):
        role = Role(**roleData.model_dump())
        self.session.add(role)  
        await self.session.commit()
        await self.session.refresh(role)  
        return role