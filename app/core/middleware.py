import time
import uuid
from fastapi import Request
from jose import jwt, JWTError

from app.core.config import SECRET_KEY, ALGORITHM
from app.core.logger import setup_logger

logger = setup_logger()


def extract_user_id(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("user_id")
    except JWTError:
        return None


async def logging_middleware(request: Request, call_next):
    request_id = str(uuid.uuid4())
    start_time = time.time()

    # Default user_id
    user_id = None

    # Extract token if present
    auth_header = request.headers.get("authorization")
    if auth_header and auth_header.startswith("Bearer "):
        token = auth_header.split(" ")[1]
        user_id = extract_user_id(token)

    # Process request
    response = await call_next(request)

    duration_ms = round((time.time() - start_time) * 1000, 2)

    log_data = {
        "request_id": request_id,
        "user_id": user_id,
        "method": request.method,
        "path": request.url.path,
        "status_code": response.status_code,
        "duration_ms": duration_ms
    }

    logger.info(log_data)

    return response