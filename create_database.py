import sys
import os
from sqlalchemy import create_engine, exc
from sqlalchemy_utils import create_database as create_postgresql_database
from dotenv import load_dotenv

def load_environment_variables():
    load_dotenv()

def create_database(database_url):
    engine = create_engine(database_url)

    try:
        create_postgresql_database(engine.url)
        print(f"Database created successfully: {engine.url.database}")
    except exc.DatabaseError as e:
        print(f"Error creating database: {e}")

if __name__ == "__main__":
    load_environment_variables()

    if len(sys.argv) != 1:
        print("Usage: python create_database.py")
        sys.exit(1)

    database_url = os.getenv('DATABASE_URL')

    if not database_url:
        print("DATABASE_URL not found in the environment variables.")
        sys.exit(1)

    create_database(database_url)
