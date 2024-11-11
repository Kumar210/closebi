from fastapi import APIRouter,Depends,HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from http import HTTPStatus
from .service import userService
from .schema import userResponseModel,userCreateModel,login
from typing import List
from src.config import settings
from src.utils.jwt.verify_token import admin_required
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
    try:
        # Assuming userService is a properly defined class with the `create_User` method
        new_user = await userService(session).create_User(user_created_model)
        return new_user
    except HTTPException as http_exc:
        raise http_exc
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "message": "error",
                "error": str(exc)
            }
        )



@user_router.get("/{user_id}",status_code=HTTPStatus.CREATED)
async def getUserbyID(
    user_id:str,
    session:AsyncSession=Depends(get_session)):
    pass


@user_router.post("/login",status_code=HTTPStatus.CREATED)
async def login(loginData:login,session:AsyncSession=Depends(get_session)):
    users = await userService(session).login(loginData,settings.secretKey)
    return users




