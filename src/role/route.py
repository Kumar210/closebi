from fastapi import APIRouter,Depends,HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from http import HTTPStatus
from .service import roleService
from .schema import roleCreateModel,roleResponseModel
from typing import List

role_router =APIRouter(
    prefix="/Permission"
)


@role_router.get("/", response_model=List[roleResponseModel])
async def get_userDetails(session:AsyncSession=Depends(get_session)):
    users = await roleService(session).get_all_user()
    return users


@role_router.post("/create", status_code=HTTPStatus.CREATED)
async def create(
    roleModel: roleCreateModel,
    session: AsyncSession = Depends(get_session)):
    try:
        new_role = await roleService(session).createRole(roleModel)
        return {
            "message": "created successfully",
            "data": new_role
        }
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