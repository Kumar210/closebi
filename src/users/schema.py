from src.db.models import User
from pydantic import BaseModel


class userResponseModel(User):
    pass


class userCreateModel(BaseModel):
    name:str
    email:str
    password:str
    isSuperAdmin:bool
    isClientAdmin :bool
    isClientUser:bool

class login(BaseModel):
    email:str
    password:str

