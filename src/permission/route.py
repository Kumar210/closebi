from fastapi import APIRouter,Depends,HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from http import HTTPStatus
from .service import permissionService
from .schema import permissionResponseModel,permissionCreateModel
from typing import List
from src.config import settings
from src.utils.jwt.verify_token import admin_required
permission_router =APIRouter(
    prefix="/Permission"
)


@permission_router.get("/", response_model=List[permissionResponseModel])
async def get_userDetails(session:AsyncSession=Depends(get_session)):
    users = await permissionService(session).get_all_user()
    return users


@permission_router.post("/create", status_code=HTTPStatus.CREATED)
async def create(
    master_created_model: permissionCreateModel,
    session: AsyncSession = Depends(get_session)):
    try:
        new_user = await permissionService(session).create_gcb(master_created_model)
        return {
            "message": "created successfully",
            "data": new_user
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
