from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi import HTTPException
from src.db.models import Call_Log
from .schema import call_log_createModel
from sqlmodel import select

class call_log_Services:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_call_log_(self):
        statement = select(Call_Log).order_by(Call_Log.created_at)
        result = await self.session.exec(statement)
        return result.all()

    async def create_call_log(self, call_log__data: call_log_createModel):
        new_google_analatics_ = Call_Log(**call_log__data.model_dump())
        self.session.add(new_google_analatics_)  # Just use `self.session.add()` here, no need for `await`
        await self.session.commit()
        await self.session.refresh(new_google_analatics_)  # Refresh the instance with the database state
        return new_google_analatics_
    
    async def call_log__getByID(self,id):
        statement = select(Call_Log).where(Call_Log.id == id)
        result = await self.session.exec(statement)
        return result.first()
    
    
 
    async def update_call_log(self,call_log_id:str,updated_data:call_log_createModel):
        statement = select(Call_Log).where(Call_Log.id == call_log_id)
        result = await self.session.exec(statement)
        call_log_data = result.first()

        if not call_log_data:
            raise HTTPException(status_code=404, detail=f"call_log with ID {call_log_id} not found") 

        for key , value in updated_data.model_dump().items():
            setattr(call_log_data,key,value)
        await self.session.commit()

        return call_log_data
    
    



