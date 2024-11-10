# from src.db.models import MasterData
from pydantic import BaseModel,Field
from typing import List
from datetime import datetime,timezone
from typing import Optional,Dict
from sqlalchemy.dialects.postgresql import JSON as pgJSON

class call_log_createModel(BaseModel):
    brand_id: str
    mobile_no:str
    call_status:str
    call_date_time: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    call_duration:int
    ring_duration:int
    enquiry_about:str
    record_file_path :str
    summary:str
    additional_data:str

    class Config:
        orm_mode = True  # Enables compatibility with ORM models (like SQLAlchemy)

class call_log_updateModel(BaseModel):
    brand_id: str
    mobile_no:str
    call_status:str
    call_date_time: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    call_duration:int
    ring_duration:int
    enquiry_about:str
    record_file_path :str
    summary:str
    additional_data:str

    class Config:
        orm_mode = True
    

