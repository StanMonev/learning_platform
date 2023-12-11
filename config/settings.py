import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from fastapi_limiter import FastAPILimiter
from fastapi_cache import FastAPICache

# Load environment variables from .env
load_dotenv()

# Database configuration
DATABASE_URL = os.getenv('DATABASE_URL')

# Redis configuration for FastAPI Limiter
REDIS_URL = os.getenv('REDIS_URL')

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# FastAPI Limiter setup
def get_limiter():
    limiter = FastAPILimiter()
    limiter.key_func = lambda: "global"
    limiter.redis_url = REDIS_URL
    return limiter

# FastAPI Cache setup
cache = FastAPICache()

# FastAPI Cache dependencies
def get_cache():
    return cache
