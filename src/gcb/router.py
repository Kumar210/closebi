from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from http import HTTPStatus
from .service import gcb_Services
from .schema import gcb_createModel
from src.utils.date_convertion import make_timezone_naive

gcb_router = APIRouter(
    prefix="/gcb"
)

@gcb_router.get("/")
async def get_data(session: AsyncSession = Depends(get_session)):
    try:
        master = await gcb_Services(session).get_all_gcb_()
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

@gcb_router.post("/create", status_code=HTTPStatus.CREATED)
async def create(
    master_created_model: gcb_createModel,
    session: AsyncSession = Depends(get_session)):
    try:
        master_created_model.date_created = make_timezone_naive(master_created_model.date_created)
        new_user = await gcb_Services(session).create_gcb(master_created_model)
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

@gcb_router.get("/{id}", status_code=HTTPStatus.OK)
async def get_by_id(
    id: str,
    session: AsyncSession = Depends(get_session)):
    try:
        master = await gcb_Services(session).gcb__getByID(id)
        if not master:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={
                    "message": "Record not found",
                    "error": f"gcb entry with ID {id} not found"
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

@gcb_router.put("/{id}")
async def update(
    id: str,
    updated_data: gcb_createModel,
    session: AsyncSession = Depends(get_session)):
    try:
        updated_data.date_created = make_timezone_naive(updated_data.date_created)
        updated_entry = await gcb_Services(session).update_gcb(id, updated_data)
        if not updated_entry:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={
                    "message": "Record not found",
                    "error": f"gcb entry with ID {id} not found for update"
                }
            )
        return {
            "message": "updated successfully",
            "data": updated_entry
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
