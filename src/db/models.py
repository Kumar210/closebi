from sqlmodel import SQLModel, Field, Column
from uuid import UUID, uuid4
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime
from typing import Optional
from sqlalchemy.dialects.postgresql import JSON as pgJSON


class User(SQLModel, table=True):
    __tablename__ = 'users'  # Use __tablename__ instead of __name__
    
    id: UUID = Field(
        sa_column=Column(pg.UUID, primary_key=True, unique=True, default=uuid4)
    )
    name: str
    created_at: datetime = Field(default_factory=lambda: datetime.now())
    updated_at: datetime = Field(default_factory=lambda: datetime.now())

    def __repr__(self) -> str:
        return f"User => {self.name} at {self.created_at}"


# from sqlmodel import SQLModel, Field, Column
# from uuid import UUID, uuid4
# import sqlalchemy.dialects.postgresql as pg
# from datetime import datetime

class MasterData(SQLModel, table=True):
    __tablename__ = 'master_data'  # Name of the table in the database
    
    id: UUID = Field(
        sa_column=Column(pg.UUID, primary_key=True, unique=True, default=uuid4)
    )
    brand_id: str
    brand_name: str
    total_location: int
    total_microsite: int
    total_live_on_gmb: int
    total_ivr: int
    total_products: int
    total_pages: int
    created_at: datetime = Field(default_factory=lambda: datetime.now())
    updated_at: datetime = Field(default_factory=lambda: datetime.now())

    def __repr__(self) -> str:
        return f"MasterData => {self.brand_name} at {self.created_at}"


class Google_Analytics(SQLModel, table=True):
    __tablename__ = 'ga_log'  # Name of the table in the database
    
    id: UUID = Field(
        sa_column=Column(pg.UUID, primary_key=True, unique=True, default=uuid4)
    )
    brand_id: str
    new_users: int
    returning_users: int
    total_engagement_time: int
    top_countries_visits: Optional[dict] = Field(
        default_factory=dict, sa_column=Column(pgJSON)
    )
    top_cities_visits: Optional[dict] = Field(
        default_factory=dict, sa_column=Column(pgJSON)
    )
    date_created: datetime
    additional_data: Optional[dict] = Field(
        default_factory=dict, sa_column=Column(pgJSON)
    )
    created_at: datetime = Field(default_factory=lambda: datetime.now())
    updated_at: datetime = Field(default_factory=lambda: datetime.now())

    def __repr__(self) -> str:
        return f"MasterData => {self.brand_name} at {self.created_at}"
