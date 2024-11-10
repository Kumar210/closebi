from fastapi import APIRouter,Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from http import HTTPStatus
from .service import gcb_Services
from .schema import gcb_createModel
from typing import List
from src.utils.date_convertion import make_timezone_naive
gcb_router =APIRouter(
    prefix="/gcb"
)

@gcb_router.get("/")
async def get_data(session:AsyncSession=Depends(get_session)):
    master = await gcb_Services(session).get_all_gcb_()
    return {
        "message":"sucessful",
        "data":master
    }

@gcb_router.post("/create",status_code=HTTPStatus.CREATED)
async def create(
    master_created_model:gcb_createModel,
    session:AsyncSession=Depends(get_session)):
    master_created_model.date_created = make_timezone_naive(master_created_model.date_created)

    new_user = await gcb_Services(session).create_gcb(master_created_model)
    return {
        "message":"created Sucessfull",
        "data":new_user
    }


@gcb_router.get("/{id}",status_code=HTTPStatus.CREATED)
async def get_by_id(
    id:str,
    session:AsyncSession=Depends(get_session)):
    print(id)
    master=await gcb_Services(session).gcb__getByID(id)
    return{
        "message" :"sucessful",
        "data":master
    }


@gcb_router.put("/{id}")
async def update(id:str,
                        updated_data:gcb_createModel,
                        session:AsyncSession = Depends(get_session)):
    print(updated_data)
    updatedata = await gcb_Services(session).update_gcb(id,updated_data)

    return updatedata
    






