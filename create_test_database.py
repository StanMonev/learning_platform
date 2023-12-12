# init_test.py
import sys
import os
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database as create_postgresql_database
from alembic import command
from alembic.config import Config
from dotenv import load_dotenv

def load_environment_variables():
    # Specify the path to the .env.test file
    env_file_path = os.path.join(os.path.dirname(__file__), '.env.test')

    # Load environment variables from the .env.test file
    load_dotenv(env_file_path)

def create_test_database(database_url):
    engine = create_engine(database_url)
    
    try:
        create_postgresql_database(engine.url)
        print(f"Test database created successfully: {engine.url.database}")
    except Exception as e:
        print(f"Error creating test database: {e}")

def apply_migrations():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")
    print("Migrations applied successfully")

if __name__ == "__main__":
    load_environment_variables()

    # Set the test database URL
    database_url = os.getenv('DATABASE_URL')
    redis_url = os.getenv('REDIS_URL')

    if not database_url:
        print("DATABASE_URL not found in the environment variables.")
        sys.exit(1)

    create_test_database(database_url)
    apply_migrations()
