from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from http import HTTPStatus
from .service import call_log_Services
from .schema import call_log_createModel
from typing import List
from src.utils.date_convertion import make_timezone_naive

call_log_router = APIRouter(
    prefix="/call_log"
)

@call_log_router.get("/")
async def get_data(session: AsyncSession = Depends(get_session)):
    try:
        master = await call_log_Services(session).get_all_call_log_()
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


@call_log_router.post("/create", status_code=HTTPStatus.CREATED)
async def create(
    master_created_model: call_log_createModel,
    session: AsyncSession = Depends(get_session)):
    try:
        master_created_model.call_date_time = make_timezone_naive(master_created_model.call_date_time)
        new_user = await call_log_Services(session).create_call_log(master_created_model)
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


@call_log_router.get("/{id}", status_code=HTTPStatus.CREATED)
async def get_by_id(
    id: str,
    session: AsyncSession = Depends(get_session)):
    try:
        master = await call_log_Services(session).call_log__getByID(id)
        if not master:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={
                    "message": "Record not found",
                    "error": f"call_log with ID {id} not found"
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


@call_log_router.put("/{id}")
async def update(
    id: str,
    updated_data: call_log_createModel,
    session: AsyncSession = Depends(get_session)):
    try:
        updated_data.call_date_time = make_timezone_naive(updated_data.call_date_time)
        updated_data = await call_log_Services(session).update_call_log(id, updated_data)
        if not updated_data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={
                    "message": "Record not found",
                    "error": f"call_log with ID {id} not found for update"
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
