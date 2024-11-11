from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi import HTTPException
from src.db.models import GCB
from .schema import gcb_createModel
from sqlmodel import select

class gcb_Services:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_gcb_(self):
        statement = select(GCB).order_by(GCB.created_at)
        result = await self.session.exec(statement)
        return result.all()

    async def create_gcb(self, gcb__data: gcb_createModel):
        new_google_analatics_ = GCB(**gcb__data.model_dump())
        self.session.add(new_google_analatics_)  
        await self.session.commit()
        await self.session.refresh(new_google_analatics_)  
        return new_google_analatics_
    
    async def gcb__getByID(self,id):
        statement = select(GCB).where(GCB.id == id)
        result = await self.session.exec(statement)
        return result.first()
    
    
 
    async def update_gcb(self,gcb_id:str,updated_data:gcb_createModel):
        statement = select(GCB).where(GCB.id == gcb_id)
        result = await self.session.exec(statement)
        gcb_data = result.first()

        if not gcb_data:
            raise HTTPException(status_code=404, detail=f"GCB with ID {gcb_id} not found") 

        for key , value in updated_data.model_dump().items():
            setattr(gcb_data,key,value)
        await self.session.commit()

        return gcb_data
    
    



