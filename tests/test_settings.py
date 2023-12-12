from config.settings import Settings
from unittest.mock import Mock

class TestSettings(Settings):
    database_url: str
    redis_url: str

    class Config:
        env_file = ".env.test"

    def get_redis(self):
        # Create a mock for the get_redis function
        mock_redis = Mock()
        return lambda: mock_redis