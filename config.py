
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
    BEDROCK_MODEL = os.getenv("BEDROCK_MODEL")
    
    # Database settings
    DATABASE_URL = os.getenv("DATABASE_URL")
    
    # Server settings
    BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:8000")
    
    # JWT settings
    SECRET_KEY = os.getenv("SECRET_KEY", "production")
    ALGORITHM = os.getenv("ALGORITHM", "hash")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

settings = Settings()
