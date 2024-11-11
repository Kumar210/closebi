from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from http import HTTPStatus
from .service import sc_log_Services
from .schema import sc_log_createModel
from typing import List
from src.utils.date_convertion import make_timezone_naive

sc_log_router = APIRouter(
    prefix="/sc_log"
)

@sc_log_router.get("/")
async def get_data(session: AsyncSession = Depends(get_session)):
    try:
        master = await sc_log_Services(session).get_all_sc_log_()
        return {
            "message": "successful",
            "data": master
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

@sc_log_router.post("/create", status_code=HTTPStatus.CREATED)
async def create(
    master_created_model: sc_log_createModel,
    session: AsyncSession = Depends(get_session)):
    try:
        new_user = await sc_log_Services(session).create_sc_log(master_created_model)
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

@sc_log_router.get("/{id}", status_code=HTTPStatus.OK)
async def get_by_id(
    id: str,
    session: AsyncSession = Depends(get_session)):
    try:
        master = await sc_log_Services(session).sc_log__getByID(id)
        if not master:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={
                    "message": "Record not found",
                    "error": f"SC log with ID {id} not found"
                }
            )
        return {
            "message": "successful",
            "data": master
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

@sc_log_router.put("/{id}")
async def update(
    id: str,
    updated_data: sc_log_createModel,
    session: AsyncSession = Depends(get_session)):
    try:
        updated_data = await sc_log_Services(session).update_sc_log(id, updated_data)
        if not updated_data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={
                    "message": "Record not found",
                    "error": f"SC log with ID {id} not found for update"
                }
            )
        return {
            "message": "updated successfully",
            "data": updated_data
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
