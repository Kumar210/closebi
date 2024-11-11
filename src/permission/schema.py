from src.db.models import Permission
from pydantic import BaseModel


class permissionResponseModel(Permission):
    pass


class permissionCreateModel(BaseModel):
    name:str


