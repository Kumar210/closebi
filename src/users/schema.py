from src.db.models import User
from pydantic import BaseModel


class userResponseModel(User):
    pass


class userCreateModel(BaseModel):
    name:str 
    

