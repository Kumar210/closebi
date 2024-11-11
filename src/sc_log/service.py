from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi import HTTPException
from src.db.models import Sc_Log
from .schema import sc_log_createModel
from sqlmodel import select

class sc_log_Services:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_sc_log_(self):
        statement = select(Sc_Log).order_by(Sc_Log.created_at)
        result = await self.session.exec(statement)
        return result.all()

    async def create_sc_log(self, sc_log__data: sc_log_createModel):
        new_google_analatics_ = Sc_Log(**sc_log__data.model_dump())
        self.session.add(new_google_analatics_)  
        await self.session.commit()
        await self.session.refresh(new_google_analatics_)  
        return new_google_analatics_
    
    async def sc_log__getByID(self,id):
        statement = select(Sc_Log).where(Sc_Log.id == id)
        result = await self.session.exec(statement)
        return result.first()
    
    
 
    async def update_sc_log(self,sc_log_id:str,updated_data:sc_log_createModel):
        statement = select(Sc_Log).where(Sc_Log.id == sc_log_id)
        result = await self.session.exec(statement)
        sc_log_data = result.first()

        if not sc_log_data:
            raise HTTPException(status_code=404, detail=f"sc_log with ID {sc_log_id} not found") 

        for key , value in updated_data.model_dump().items():
            setattr(sc_log_data,key,value)
        await self.session.commit()

        return sc_log_data
    
    



