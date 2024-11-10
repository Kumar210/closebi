from fastapi import APIRouter,Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from http import HTTPStatus
from .service import sc_log_Services
from .schema import sc_log_createModel
from typing import List
from src.utils.date_convertion import make_timezone_naive
sc_log_router =APIRouter(
    prefix="/sc_log"
)

@sc_log_router.get("/")
async def get_data(session:AsyncSession=Depends(get_session)):
    master = await sc_log_Services(session).get_all_sc_log_()
    return {
        "message":"sucessful",
        "data":master
    }




@sc_log_router.post("/create",status_code=HTTPStatus.CREATED)
async def create(
    master_created_model:sc_log_createModel,
    session:AsyncSession=Depends(get_session)):
    new_user = await sc_log_Services(session).create_sc_log(master_created_model)
    return {
        "message":"created Sucessfull",
        "data":new_user
    }


@sc_log_router.get("/{id}",status_code=HTTPStatus.CREATED)
async def get_by_id(
    id:str,
    session:AsyncSession=Depends(get_session)):
    print(id)
    master=await sc_log_Services(session).sc_log__getByID(id)
    return{
        "message" :"sucessful",
        "data":master
    }


@sc_log_router.put("/{id}")
async def update(id:str,
                        updated_data:sc_log_createModel,
                        session:AsyncSession = Depends(get_session)):
    print(updated_data)
    updatedata = await sc_log_Services(session).update_sc_log(id,updated_data)

    return updatedata
    






