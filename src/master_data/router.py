from fastapi import APIRouter,Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from http import HTTPStatus
from .service import masterServices
from .schema import masterCreateModel,masterUpdateModel
from typing import List
master_router =APIRouter(
    prefix="/masterdata"
)

@master_router.get("/")
async def get_masterDetails(session:AsyncSession=Depends(get_session)):
    master = await masterServices(session).get_all_master()
    return {
        "message":"sucessful",
        "data":master
    }




@master_router.post("/create",status_code=HTTPStatus.CREATED)
async def create_master(
    master_created_model:masterCreateModel,
    session:AsyncSession=Depends(get_session)):
    new_user = await masterServices(session).create_master(master_created_model)
    return {
        "message":"created Sucessfull",
        "data":new_user
    }


@master_router.get("/{id}",status_code=HTTPStatus.CREATED)
async def get_master_id(
    id:str,
    session:AsyncSession=Depends(get_session)):
    print(id)
    master=await masterServices(session).master_getByID(id)
    return{
        "message" :"sucessful",
        "data":master
    }


@master_router.put("/{id}")
async def update_master(id:str,
                        updated_data:masterCreateModel,
                        session:AsyncSession = Depends(get_session)):
    print(updated_data)
    updatedata = await masterServices(session).update_master(id,updated_data)

    return updatedata
    






