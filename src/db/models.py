from sqlmodel import SQLModel, Field, Column
from uuid import UUID, uuid4
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime, timezone
from typing import Optional
from sqlalchemy.dialects.postgresql import JSON as pgJSON
from sqlalchemy import String,ForeignKey,Integer
from sqlalchemy.orm import relationship,Mapped,mapped_column


class User(SQLModel, table=True):
        __tablename__ = 'users'  
        
        id: UUID = Field(
            sa_column=Column(pg.UUID(as_uuid=True), primary_key=True, unique=True, default=uuid4)
        )
        name: str
        email: str = Field(sa_column=Column(String, unique=True, index=True))  # Fixed email definition
        password: str
        role_id: UUID = Field(default=None, foreign_key="role.id", primary_key=True)

        role_id = relationship("Role")
        created_at: datetime = Field(default_factory=lambda: datetime.now())
        updated_at: datetime = Field(default_factory=lambda: datetime.now())


        def __repr__(self) -> str:
            return f"User => {self.name} at {self.created_at}"


class MasterData(SQLModel, table=True):
    __tablename__ = "master_data"  # Name of the table in the database

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
    
    
class Permission(SQLModel, table=True):
    __tablename__ = "permission"  # Name of the table in the database

    id: UUID = Field(
        sa_column=Column(pg.UUID, primary_key=True, unique=True, default=uuid4)
    )
    name:str
    created_at: datetime = Field(default_factory=lambda: datetime.now())
    updated_at: datetime = Field(default_factory=lambda: datetime.now())

    def __repr__(self) -> str:
        return f"Permission => {self.brand_name} at {self.created_at}"


class Google_Analytics(SQLModel, table=True):
    __tablename__ = "ga_log"  # Name of the table in the database

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
    date_created: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    additional_data: Optional[dict] = Field(
        default_factory=dict, sa_column=Column(pgJSON)
    )
    created_at: datetime = Field(default_factory=lambda: datetime.now())
    updated_at: datetime = Field(default_factory=lambda: datetime.now())

    def __repr__(self) -> str:
        return f"MasterData => {self.brand_id} at {self.created_at}"


class GCB(SQLModel, table=True):
    __tablename__ = "gcb"  # Name of the table in the database

    id: UUID = Field(
        sa_column=Column(pg.UUID, primary_key=True, unique=True, default=uuid4)
    )
    brand_id: str
    search_impressions: Optional[dict] = Field(
        default_factory=dict, sa_column=Column(pgJSON)
    )
    map_impressions: Optional[dict] = Field(
        default_factory=dict, sa_column=Column(pgJSON)
    )
    drive_driections: int
    date_created: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    created_at: datetime = Field(default_factory=lambda: datetime.now())
    updated_at: datetime = Field(default_factory=lambda: datetime.now())

    def __repr__(self) -> str:
        return f"MasterData => {self.brand_id} at {self.created_at}"


class Sc_Log(SQLModel, table=True):
    __tablename__ = "sc_log"  # Name of the table in the database

    id: UUID = Field(
        sa_column=Column(pg.UUID, primary_key=True, unique=True, default=uuid4)
    )
    brand_id: str
    impressions: Optional[dict] = Field(default_factory=dict, sa_column=Column(pgJSON))
    clicks: Optional[dict] = Field(default_factory=dict, sa_column=Column(pgJSON))
    top_countries: Optional[dict] = Field(
        default_factory=dict, sa_column=Column(pgJSON)
    )
    avg_ctr: int
    avg_position: int
    created_at: datetime = Field(default_factory=lambda: datetime.now())
    updated_at: datetime = Field(default_factory=lambda: datetime.now())

    def __repr__(self) -> str:
        return f"Sc_Log => {self.brand_id} at {self.created_at}"


class Call_Log(SQLModel, table=True):
    __tablename__ = "call_log"  # Name of the table in the database

    id: UUID = Field(
        sa_column=Column(pg.UUID, primary_key=True, unique=True, default=uuid4)
    )
    brand_id: str
    mobile_no: str
    call_status: str
    call_date_time: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    call_duration: int
    ring_duration: int
    enquiry_about: str
    record_file_path: str
    summary: str
    additional_data: str
    created_at: datetime = Field(default_factory=lambda: datetime.now())
    updated_at: datetime = Field(default_factory=lambda: datetime.now())

    def __repr__(self) -> str:
        return f"Sc_Log => {self.brand_id} at {self.created_at}"


class Invoice_Log(SQLModel, table=True):
    __tablename__ = "invoice_log"  # Name of the table in the database

    id: UUID = Field(
        sa_column=Column(pg.UUID, primary_key=True, unique=True, default=uuid4)
    )
    brand_id: str
    customer_phone: str
    invoice_date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    total_amount: str
    additional_data: Optional[dict] = Field(
        default_factory=dict, sa_column=Column(pgJSON)
    )
    sync_status: bool
    sync_time: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    created_at: datetime = Field(default_factory=lambda: datetime.now())
    updated_at: datetime = Field(default_factory=lambda: datetime.now())

    def __repr__(self) -> str:
        return f"Sc_Log => {self.brand_id} at {self.created_at}"


class RolePermission(SQLModel,table=True):
    __tablename__  = "rolePermission"
        
    id: UUID = Field(
        sa_column=Column(pg.UUID, primary_key=True, unique=True, default=uuid4)
    )
    # role_id:Mapped[int] = mapped_column(ForeignKey("role.id"), primary_key=True)
    role_id: UUID = Field(default=None, foreign_key="role.id", primary_key=True)
    permission_id: UUID = Field(default=None, foreign_key="permission.id", primary_key=True)

    created_at: datetime = Field(default_factory=lambda: datetime.now())
    updated_at: datetime = Field(default_factory=lambda: datetime.now())

    role_id = relationship("Role")
    permission_id = relationship("Permission")
    def __repr__(self) -> str:
        return f"Sc_Log => {self.role_id} at {self.created_at}"
        
        
class Permission(SQLModel, table=True):
    __tablename__ = "permissions" 

    id: UUID = Field(default_factory=uuid4 ,primary_key=True, unique=True)
    name: str
    created_at: datetime = Field(default_factory=lambda: datetime.now())
    updated_at: datetime = Field(default_factory=lambda: datetime.now())

    def __repr__(self) -> str:
        return f"Permission => {self.name} at {self.created_at}"


# Role table
class Role(SQLModel, table=True):
    __tablename__ = "role"

    id: UUID = Field(
        sa_column=Column(pg.UUID, primary_key=True, unique=True, default=uuid4)
    )
    name: str
    created_at: datetime = Field(default_factory=lambda: datetime.now())
    updated_at: datetime = Field(default_factory=lambda: datetime.now())
    # permission: Mapped[List["RolePermission"]] = relationship(back_populates="role")

    def __repr__(self) -> str:
        return f"Role => {self.name} at {self.created_at}"
