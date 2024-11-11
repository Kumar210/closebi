# from src.db.models import MasterData
from pydantic import BaseModel,Field
from typing import List
from datetime import datetime,timezone
from typing import Optional,Dict
from sqlalchemy.dialects.postgresql import JSON as pgJSON
class impression_model(BaseModel):
    device_name: str
    count: int
class gcb_createModel(BaseModel):
    brand_id: str
    search_impressions: Optional[impression_model] = Field(default_factory=impression_model)
    map_impressions: Optional[impression_model] = Field(default_factory=impression_model)
    drive_driections: int
    date_created: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Config:
        orm_mode = True  # Enables compatibility with ORM models (like SQLAlchemy)

class gcb_updateModel(BaseModel):
    brand_id: str
    search_impressions: Optional[impression_model] = Field(default_factory=impression_model)
    map_impressions: Optional[impression_model] = Field(default_factory=impression_model)
    drive_driections: int
    date_created: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Config:
        orm_mode = True
    

