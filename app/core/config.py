import os
from dotenv import load_dotenv

SECRET_KEY = "your-secret-key"  # later move to .env
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_MINUTES = 1440  # 1 day

load_dotenv()