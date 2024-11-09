# from src.db.models import MasterData
from pydantic import BaseModel
from typing import List





class masterCreateModel(BaseModel):
    brand_id: str
    brand_name: str
    total_location: int
    total_microsite: int
    total_live_on_gmb: int
    total_ivr: int
    total_products: int
    total_pages: int


class masterUpdateModel(BaseModel):
    brand_id: str
    brand_name: str
    total_location: int
    total_microsite: int
    total_live_on_gmb: int
    total_ivr: int
    total_products: int
    total_pages: int

    class Config:
        orm_mode = True
    

