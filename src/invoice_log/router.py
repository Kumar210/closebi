from fastapi import APIRouter,Depends,HTTPException,status
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from http import HTTPStatus
from .service import invoice_log_Services
from .schema import invoice_log_createModel
from typing import List
from src.utils.date_convertion import make_timezone_naive

invoice_log_router =APIRouter(
    prefix="/invoice_log"
)

@invoice_log_router.get("/")
async def get_data(session: AsyncSession = Depends(get_session)):
    try:
        master = await invoice_log_Services(session).get_all_invoice_log_()
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

@invoice_log_router.post("/create",status_code=HTTPStatus.CREATED)
async def create(
    master_created_model: invoice_log_createModel,
    session: AsyncSession = Depends(get_session)
):
    try:
        master_created_model.invoice_date = make_timezone_naive(master_created_model.invoice_date)
        master_created_model.sync_time = make_timezone_naive(master_created_model.sync_time)
        new_user = await invoice_log_Services(session).create_invoice_log(master_created_model)
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

@invoice_log_router.get("/{id}", status_code=HTTPStatus.OK)
async def get_by_id(
    id: str,
    session: AsyncSession = Depends(get_session)
):
    try:
        master = await invoice_log_Services(session).invoice_log__getByID(id)
        if not master:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No data found for the given ID"
            )
        
        return {
            "message": "Successful",
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

@invoice_log_router.put("/{id}")
async def update(
    id: str,
    updated_data: invoice_log_createModel,
    session: AsyncSession = Depends(get_session)
):
    try:
        updated_data.invoice_date = make_timezone_naive(updated_data.invoice_date)
        updated_data.sync_time = make_timezone_naive(updated_data.sync_time)
        updatedata = await invoice_log_Services(session).update_invoice_log(id, updated_data)
        if not updatedata:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No data found to update"
            )

        return {
            "message": "Updated successfully",
            "data": updatedata
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






