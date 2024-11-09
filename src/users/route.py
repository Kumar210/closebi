from fastapi import APIRouter,Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from http import HTTPStatus
from .service import userService
from .schema import userResponseModel,userCreateModel
from typing import List
user_router =APIRouter(
    prefix="/user"
)

@user_router.get("/", response_model=List[userResponseModel])
async def get_userDetails(session:AsyncSession=Depends(get_session)):
    users = await userService(session).get_all_user()
    return users





@user_router.post("/create",status_code=HTTPStatus.CREATED)
async def create_user(
    user_created_model:userCreateModel,
    session:AsyncSession=Depends(get_session)):
    new_user = await userService(session).create_User(user_created_model)
    return new_user


@user_router.get("/{user_id}",status_code=HTTPStatus.CREATED)
async def getUserbyID(
    user_id:str,
    session:AsyncSession=Depends(get_session)):
    print(user_id)
    pass





