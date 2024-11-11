from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from http import HTTPStatus
from .service import masterServices
from .schema import masterCreateModel, masterUpdateModel
from typing import List

master_router = APIRouter(
    prefix="/masterdata"
)

@master_router.get("/")
async def get_masterDetails(session: AsyncSession = Depends(get_session)):
    try:
        master = await masterServices(session).get_all_master()
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

@master_router.post("/create", status_code=HTTPStatus.CREATED)
async def create_master(
    master_created_model: masterCreateModel,
    session: AsyncSession = Depends(get_session)):
    try:
        new_user = await masterServices(session).create_master(master_created_model)
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

@master_router.get("/{id}", status_code=HTTPStatus.OK)
async def get_master_id(
    id: str,
    session: AsyncSession = Depends(get_session)):
    try:
        master = await masterServices(session).master_getByID(id)
        if not master:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={
                    "message": "Record not found",
                    "error": f"Master data with ID {id} not found"
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

@master_router.put("/{id}")
async def update_master(
    id: str,
    updated_data: masterUpdateModel,
    session: AsyncSession = Depends(get_session)):
    try:
        updated_data = await masterServices(session).update_master(id, updated_data)
        if not updated_data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={
                    "message": "Record not found",
                    "error": f"Master data with ID {id} not found for update"
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
