from fastapi import APIRouter,Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from http import HTTPStatus
from .service import google_analatics_Services
from .schema import google_analatics_CreateModel
from typing import List
from src.utils.date_convertion import make_timezone_naive
analytics_router =APIRouter(
    prefix="/analytics"
)

@analytics_router.get("/")
async def get_data(session:AsyncSession=Depends(get_session)):
    master = await google_analatics_Services(session).get_all_google_analatics_()
    return {
        "message":"sucessful",
        "data":master
    }




@analytics_router.post("/create",status_code=HTTPStatus.CREATED)
async def create(
    master_created_model:google_analatics_CreateModel,
    session:AsyncSession=Depends(get_session)):
    master_created_model.date_created = make_timezone_naive(master_created_model.date_created)

    new_user = await google_analatics_Services(session).create_google_analatics(master_created_model)
    return {
        "message":"created Sucessfull",
        "data":new_user
    }


@analytics_router.get("/{id}",status_code=HTTPStatus.CREATED)
async def get_by_id(
    id:str,
    session:AsyncSession=Depends(get_session)):
    print(id)
    master=await google_analatics_Services(session).google_analatics__getByID(id)
    return{
        "message" :"sucessful",
        "data":master
    }


@analytics_router.put("/{id}")
async def update(id:str,
                        updated_data:google_analatics_CreateModel,
                        session:AsyncSession = Depends(get_session)):
    print(updated_data)
    updatedata = await google_analatics_Services(session).update_google_analatics_(id,updated_data)

    return updatedata
    






