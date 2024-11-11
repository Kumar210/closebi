import uuid
from fastapi import HTTPException,Depends,FastAPI
import jwt
from datetime import datetime, timedelta
from src.config import settings
from fastapi import status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Function to generate JWT token
def create_jwt_token(user_id: uuid.UUID, email: str, secret_key: str, algorithm: str = settings.algorithm):
    # Ensure UUID is converted to a string
    user_id_str = str(user_id)
    
    expiration = datetime.utcnow() + timedelta(hours=23)  # Token expires in 23 hour
    payload = {
        "sub": user_id_str,  # Using string representation of UUID
        "email": email,
        "exp": expiration
    }
    
    return jwt.encode(payload, secret_key, algorithm=algorithm)