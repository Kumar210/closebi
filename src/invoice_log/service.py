from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi import HTTPException
from src.db.models import Invoice_Log
from .schema import invoice_log_createModel
from sqlmodel import select

class invoice_log_Services:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_invoice_log_(self):
        statement = select(Invoice_Log).order_by(Invoice_Log.created_at)
        result = await self.session.exec(statement)
        return result.all()

    async def create_invoice_log(self, invoice_log__data: invoice_log_createModel):
        new_google_analatics_ = Invoice_Log(**invoice_log__data.model_dump())
        self.session.add(new_google_analatics_)  
        await self.session.commit()
        await self.session.refresh(new_google_analatics_)  
        return new_google_analatics_
    
    async def invoice_log__getByID(self,id):
        statement = select(Invoice_Log).where(Invoice_Log.id == id)
        result = await self.session.exec(statement)
        invoice_data =result.first()
        if not invoice_data:
            raise HTTPException(
                status_code=404,
                detail={
                    "message": "Invoice id not found",
                    "error": f"invoice_log with ID {id} not found"
                }
            )
        return invoice_data
    
    async def update_invoice_log(self,invoice_log_id:str,updated_data:invoice_log_createModel):
        statement = select(Invoice_Log).where(Invoice_Log.id == invoice_log_id)
        result = await self.session.exec(statement)
        invoice_log_data = result.first()

        if not invoice_log_data:
            raise HTTPException(
                status_code=404,
                detail={
                    "message": "Invoice id not found",
                    "error": f"invoice_log with ID {invoice_log_id} not found"
                }
            )
        

        for key , value in updated_data.model_dump().items():
            setattr(invoice_log_data,key,value)
        await self.session.commit()

        return invoice_log_data
    
    



