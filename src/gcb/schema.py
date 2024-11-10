# from src.db.models import MasterData
from pydantic import BaseModel,Field
from typing import List
from datetime import datetime,timezone
from typing import Optional,Dict
from sqlalchemy.dialects.postgresql import JSON as pgJSON

class gcb_createModel(BaseModel):
    brand_id: str
    search_impressions: Optional[dict] = Field(default_factory=dict)
    map_impressions: Optional[dict] = Field(default_factory=dict)
    drive_driections: int
    date_created: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Config:
        orm_mode = True  # Enables compatibility with ORM models (like SQLAlchemy)

class gcb_updateModel(BaseModel):
    brand_id: str
    search_impressions: Optional[dict] = Field(default_factory=dict)
    map_impressions: Optional[dict] = Field(default_factory=dict)
    drive_driections: int
    date_created: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    class Config:
        orm_mode = True
    

