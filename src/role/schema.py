from src.db.models import Role, RolePermission
from pydantic import BaseModel


class roleResponseModel(Role):
    pass


class roleCreateModel(BaseModel):
    name:str
    

class rolePermissionResponseModel(RolePermission):
    pass


class rolePermissionCreateModel(BaseModel):
    role_id:str
    permission_id:str
