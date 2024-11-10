# from src.db.models import MasterData
from pydantic import BaseModel,Field
from typing import List
from datetime import datetime,timezone
from typing import Optional,Dict
from sqlalchemy.dialects.postgresql import JSON as pgJSON

class sc_log_createModel(BaseModel):
    brand_id: str
    impressions: Optional[dict] = Field(default_factory=dict)
    clicks: Optional[dict] = Field(default_factory=dict)
    top_countries: Optional[dict] = Field(default_factory=dict)
    avg_ctr :int
    avg_position:int

    class Config:
        orm_mode = True  

class sc_log_updateModel(BaseModel):
    brand_id: str
    impressions: Optional[dict] = Field(default_factory=dict)
    clicks: Optional[dict] = Field(default_factory=dict)
    top_countries: Optional[dict] = Field(default_factory=dict)
    avg_ctr :int
    avg_position:int

    class Config:
        orm_mode = True
    

