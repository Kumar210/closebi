from src.db.models import Role
from pydantic import BaseModel


class roleResponseModel(Role):
    pass


class roleCreateModel(BaseModel):
    name:str


