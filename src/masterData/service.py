from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi import HTTPException
from src.db.models import MasterData
from sqlalchemy.orm.exc import NoResultFound  
from .schema import masterCreateModel
from sqlmodel import select

class masterServices:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_master(self):
        statement = select(MasterData).order_by(MasterData.created_at)
        result = await self.session.exec(statement)
        return result.all()

    async def create_master(self, master_data: masterCreateModel):
        new_master = MasterData(**master_data.model_dump())
        self.session.add(new_master)  # Just use `self.session.add()` here, no need for `await`
        await self.session.commit()
        await self.session.refresh(new_master)  # Refresh the instance with the database state
        return new_master
    
    async def master_getByID(self,id):
        statement = select(MasterData).where(MasterData.id == id)
        result = await self.session.exec(statement)
        return result.first()
    
    
 
    async def update_master(self,master_id:str,updated_data:masterCreateModel):
        statement = select(MasterData).where(MasterData.id == master_id)
        result = await self.session.exec(statement)
        master = result.first()

        if not master:
            raise HTTPException(status_code=404, detail=f"MasterData with ID {master_id} not found") 

        for key , value in updated_data.model_dump().items():
            setattr(master,key,value)
        await self.session.commit()

        return master
    
    



