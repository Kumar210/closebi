from src.db.models import Permission,RolePermission
from pydantic import BaseModel


class permissionResponseModel(Permission):
    pass


class permissionCreateModel(BaseModel):
    name:str
