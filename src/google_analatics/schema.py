# from src.db.models import MasterData
from pydantic import BaseModel,Field
from typing import List
from datetime import datetime,timezone
from typing import Optional,Dict
from sqlalchemy.dialects.postgresql import JSON as pgJSON

class google_analatics_CreateModel(BaseModel):
    brand_id: str
    new_users: int
    returning_users: int
    total_engagement_time: int
    top_countries_visits: Optional[dict] = Field(default_factory=dict)
    top_cities_visits: Optional[dict] = Field(default_factory=dict)
    date_created: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    additional_data: Optional[dict] = Field(default_factory=dict)

    class Config:
        orm_mode = True  # Enables compatibility with ORM models (like SQLAlchemy)

      
    
       


class google_analatics_UpdateModel(BaseModel):
    brand_id: str
    new_users: int
    returning_users: int
    total_engagement_time: int
    top_countries_visits: Optional[dict] = Field(default_factory=dict)
    top_cities_visits: Optional[dict] = Field(default_factory=dict)
    date_created: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    additional_data: Optional[dict] = Field(default_factory=dict)

    class Config:
        orm_mode = True
    

