from pydantic_settings import BaseSettings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import redis.asyncio as redis

class Settings(BaseSettings):
    database_url: str
    redis_url: str

    class Config:
        env_file = ".env"    
        
    # Custom method to get Redis (override)
    def get_redis(self):
        # Implement your custom logic or return a mock
        return redis.from_url(self.redis_url, encoding="utf-8", decode_responses=True)

settings = Settings()

# Engine and session intialization
engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
