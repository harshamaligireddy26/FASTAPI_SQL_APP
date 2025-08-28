from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Get DATABASE_URL from environment
DATABASE_URL = os.getenv("DATABASE_URL")

# Fix postgres:// → postgresql+psycopg://
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+psycopg://", 1)

# ✅ Engine
engine = create_engine(DATABASE_URL)

# ✅ Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ✅ Base
Base = declarative_base()
