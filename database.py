from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

# ✅ Build connection safely
DATABASE_URL = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="@#$123qweASD",  # your raw password, no encoding needed
    host="localhos",
    port=3306,               # default MySQL port
    database="fastapi_db"
)

# ✅ Engine
engine = create_engine(DATABASE_URL)

# ✅ Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ✅ Base
Base = declarative_base()
