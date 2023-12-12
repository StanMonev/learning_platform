from typing import Any
from typing import Generator

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
#this is to include backend dir in sys.path so that we can import from db,main.py

from models import model_user, model_course, model_lesson
from test_settings import TestSettings
from config.settings import SessionLocal
from routes import router
from pytest_redis.factories import redisdb

# Load environment variables from .env.test
from dotenv import load_dotenv
load_dotenv('.env.test')

settings = TestSettings()
engine = create_engine(settings.database_url)
# Use connect_args parameter only with sqlite
SessionTesting = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def start_application():
    app = FastAPI()
    app.include_router(router)
    return app


@pytest.fixture(scope="function")
def app() -> Generator[FastAPI, Any, None]:
    """
    Create a fresh database on each test case.
    """
    model_user.Base.metadata.create_all(engine)
    model_course.Base.metadata.create_all(engine)
    model_lesson.Base.metadata.create_all(engine)
    _app = start_application()
    yield _app
    model_user.Base.metadata.drop_all(engine)
    model_course.Base.metadata.drop_all(engine)
    model_lesson.Base.metadata.drop_all(engine)


@pytest.fixture(scope="function")
def db_session(app: FastAPI) -> Generator[SessionTesting, Any, None]:
    connection = engine.connect()
    transaction = connection.begin()
    session = SessionTesting(bind=connection)
    yield session  # use the session in tests.
    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope="function")
def client(
    app: FastAPI, db_session: SessionTesting, redisdb: Any
) -> Generator[TestClient, Any, None]:
    """
    Create a new FastAPI TestClient that uses the `db_session` fixture to override
    the `get_db` dependency that is injected into routes.
    """

    def _get_test_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[SessionLocal] = _get_test_db
    with TestClient(app) as client:
        yield client

@pytest.fixture
def get_redis():
    return lambda: REDIS_SERVER