from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi import HTTPException
from src.db.models import Google_Analytics
from .schema import google_analatics_CreateModel
from sqlmodel import select

class google_analatics_Services:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_google_analatics_(self):
        statement = select(Google_Analytics).order_by(Google_Analytics.created_at)
        result = await self.session.exec(statement)
        return result.all()

    async def create_google_analatics(self, google_analatics__data: google_analatics_CreateModel):
        new_google_analatics_ = Google_Analytics(**google_analatics__data.model_dump())
        self.session.add(new_google_analatics_)  # Just use `self.session.add()` here, no need for `await`
        await self.session.commit()
        await self.session.refresh(new_google_analatics_)  # Refresh the instance with the database state
        return new_google_analatics_
    
    async def google_analatics__getByID(self,id):
        statement = select(Google_Analytics).where(Google_Analytics.id == id)
        result = await self.session.exec(statement)
        return result.first()
    
    
 
    async def update_google_analatics_(self,google_analatics__id:str,updated_data:google_analatics_CreateModel):
        statement = select(Google_Analytics).where(Google_Analytics.id == google_analatics__id)
        result = await self.session.exec(statement)
        google_analatics_ = result.first()

        if not google_analatics_:
            raise HTTPException(status_code=404, detail=f"Google_Analytics with ID {google_analatics__id} not found") 

        for key , value in updated_data.model_dump().items():
            setattr(google_analatics_,key,value)
        await self.session.commit()

        return google_analatics_
    
    



