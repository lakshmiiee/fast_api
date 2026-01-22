from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
import os
from dotenv import load_dotenv

load_dotenv()

# Setup password hashing configuration
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 1. Function to hash a plain password (used during Signup)
def hash_password(password: str):
    return pwd_context.hash(password)

# 2. Function to verify a password (used during Signin)
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# 3. Function to create a JWT Access Token
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")))
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(
        to_encode, 
        os.getenv("SECRET_KEY"), 
        algorithm=os.getenv("ALGORITHM")
    )
    return encoded_jwt

def create_refresh_token(data : dict):
    to_encode = data.copy()
    expire =   datetime.utcnow() + timedelta(days=7)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        os.getenv("SECRET_KEY"),
        algorithm = os.getenv("ALGORITHM")
    )
    return encoded_jwt