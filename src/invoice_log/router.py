from fastapi import APIRouter,Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from http import HTTPStatus
from .service import invoice_log_Services
from .schema import invoice_log_createModel
from typing import List
from src.utils.date_convertion import make_timezone_naive
invoice_log_router =APIRouter(
    prefix="/invoice_log"
)

@invoice_log_router.get("/")
async def get_data(session:AsyncSession=Depends(get_session)):
    master = await invoice_log_Services(session).get_all_invoice_log_()
    return {
        "message":"sucessful",
        "data":master
    }

@invoice_log_router.post("/create",status_code=HTTPStatus.CREATED)
async def create(
    master_created_model:invoice_log_createModel,
    session:AsyncSession=Depends(get_session)):

    master_created_model.invoice_date = make_timezone_naive(master_created_model.invoice_date)
    master_created_model.sync_time = make_timezone_naive(master_created_model.sync_time)

    new_user = await invoice_log_Services(session).create_invoice_log(master_created_model)
    return {
        "message":"created Sucessfull",
        "data":new_user
    }


@invoice_log_router.get("/{id}",status_code=HTTPStatus.CREATED)
async def get_by_id(
    id:str,
    session:AsyncSession=Depends(get_session)):
    print(id)
    master=await invoice_log_Services(session).invoice_log__getByID(id)
    return{
        "message" :"sucessful",
        "data":master
    }


@invoice_log_router.put("/{id}")
async def update(id:str,
                        updated_data:invoice_log_createModel,
                        session:AsyncSession = Depends(get_session)):
    print(updated_data)
    updated_data.invoice_date = make_timezone_naive(updated_data.invoice_date)
    updated_data.sync_time = make_timezone_naive(updated_data.sync_time)
    updatedata = await invoice_log_Services(session).update_invoice_log(id,updated_data)

    return updatedata
    






