from src.db.models import Permission,RolePermission
from pydantic import BaseModel


class permissionResponseModel(Permission):
    pass


class permissionCreateModel(BaseModel):
    name:str


class RolePermissionResponseMModel(RolePermission):
    pass


class rolePermissionCreateModel(BaseModel):
    name:str
    role_id:str
    permission_id:str
    
    class Config:
        orm_mode = True
