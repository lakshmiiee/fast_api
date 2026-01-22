import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load the variables from your .env file
load_dotenv()

# Get the connection string we made earlier
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Create the engine to connect to MySQL
# 'engine' is the name main.py was looking for!
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# This creates a session factory so we can talk to the DB later
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# This is the base class for our models (used in models.py)
Base = declarative_base()

# This is a helper function to get a database connection for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()