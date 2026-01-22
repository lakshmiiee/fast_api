from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
import models, schemas, auth_utils
from database import engine, get_db

# Create the FastAPI app
app = FastAPI()

# 1. SIGNUP API
@app.post("/api/auth/signup", status_code=status.HTTP_201_CREATED)
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check if email already exists
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash the password
    hashed_pwd = auth_utils.hash_password(user.password)

    # Create new user object
    new_user = models.User(
        company_name=user.company_name,
        name=user.name,
        email=user.email,
        address=user.address,
        password=hashed_pwd
    )

    # Save to MySQL
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {"message": "User registered successfully"}

# 2. SIGNIN API
@app.post("/api/auth/signin", response_model=schemas.Token)
def signin(
    user_credentials: schemas.UserLogin,
    response: Response,
    db: Session = Depends(get_db)
    ):
    # Find user by email
    user = db.query(models.User).filter(models.User.email == user_credentials.email).first()
    
    # Check if user exists and password is correct
    if not user or not auth_utils.verify_password(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Invalid Credentials"
        )

    # Create JWT Token
    access_token = auth_utils.create_access_token(data={"user_id": user.id, "email": user.email})

    refresh_token = auth_utils.create_refresh_token(data={"user_id": user.id})

    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        max_age = 7 * 24 * 60 * 60,
        samesite="lax",
        secure=False
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": user
    }