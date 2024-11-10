# from src.db.models import MasterData
from pydantic import BaseModel,Field
from typing import List
from datetime import datetime,timezone
from typing import Optional,Dict
from sqlalchemy.dialects.postgresql import JSON as pgJSON

class invoice_log_createModel(BaseModel):
   brand_id: str
   customer_phone:str
   invoice_date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
   total_amount:str
   additional_data: Optional[dict] = Field(default_factory=dict)
   sync_status:bool
   sync_time:datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

   class Config:
     orm_mode = True  

class invoice_log_updateModel(BaseModel):
   brand_id: str
   customer_phone:str
   invoice_date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
   total_amount:str
   additional_data: Optional[dict] = Field(default_factory=dict)
   sync_status:bool
   sync_time:datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

   class Config:
      orm_mode = True
    

