from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from http import HTTPStatus
from .service import google_analatics_Services
from .schema import google_analatics_CreateModel
from src.utils.date_convertion import make_timezone_naive

analytics_router = APIRouter(
    prefix="/analytics"
)

@analytics_router.get("/")
async def get_data(session: AsyncSession = Depends(get_session)):
    try:
        master = await google_analatics_Services(session).get_all_google_analatics_()
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

@analytics_router.post("/create", status_code=HTTPStatus.CREATED)
async def create(
    master_created_model: google_analatics_CreateModel,
    session: AsyncSession = Depends(get_session)):
    try:
        master_created_model.date_created = make_timezone_naive(master_created_model.date_created)
        new_user = await google_analatics_Services(session).create_google_analatics(master_created_model)
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

@analytics_router.get("/{id}", status_code=HTTPStatus.OK)
async def get_by_id(
    id: str,
    session: AsyncSession = Depends(get_session)):
    try:
        master = await google_analatics_Services(session).google_analatics__getByID(id)
        if not master:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={
                    "message": "Record not found",
                    "error": f"Analytics entry with ID {id} not found"
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

@analytics_router.put("/{id}")
async def update(
    id: str,
    updated_data: google_analatics_CreateModel,
    session: AsyncSession = Depends(get_session)):
    try:
        updated_data.date_created = make_timezone_naive(updated_data.date_created)
        updated_entry = await google_analatics_Services(session).update_google_analatics_(id, updated_data)
        if not updated_entry:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail={
                    "message": "Record not found",
                    "error": f"Analytics entry with ID {id} not found for update"
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
