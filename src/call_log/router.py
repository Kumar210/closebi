from fastapi import APIRouter,Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from http import HTTPStatus
from .service import call_log_Services
from .schema import call_log_createModel
from typing import List
from src.utils.date_convertion import make_timezone_naive
call_log_router =APIRouter(
    prefix="/call_log"
)

@call_log_router.get("/")
async def get_data(session:AsyncSession=Depends(get_session)):
    master = await call_log_Services(session).get_all_call_log_()
    return {
        "message":"sucessful",
        "data":master
    }




@call_log_router.post("/create",status_code=HTTPStatus.CREATED)
async def create(
    master_created_model:call_log_createModel,
    session:AsyncSession=Depends(get_session)):
    master_created_model.call_date_time = make_timezone_naive(master_created_model.call_date_time)

    new_user = await call_log_Services(session).create_call_log(master_created_model)
    return {
        "message":"created Sucessfull",
        "data":new_user
    }


@call_log_router.get("/{id}",status_code=HTTPStatus.CREATED)
async def get_by_id(
    id:str,
    session:AsyncSession=Depends(get_session)):
    print(id)
    master=await call_log_Services(session).call_log__getByID(id)
    return{
        "message" :"sucessful",
        "data":master
    }


@call_log_router.put("/{id}")
async def update(id:str,
                        updated_data:call_log_createModel,
                        session:AsyncSession = Depends(get_session)):
    print(updated_data)
    updatedata = await call_log_Services(session).update_call_log(id,updated_data)

    return updatedata
    






