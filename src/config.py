from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()  # Make sure this is before using the Settings class

class Settings(BaseSettings):
    POSTGRES_URL: str
    secretKey:str
    algorithm:str
    model_config = SettingsConfigDict(
        env_file=".env",  # Ensure .env file is correctly specified
        extra="ignore"
    )

# Test loading the environment variable
settings = Settings()

# Output the settings model dump
print(settings.model_dump(),"mijjiii")
