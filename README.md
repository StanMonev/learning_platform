# Learning Platform

A learning platform backend application that enables the exchange of teaching materials between teachers and students and tracks learning progress.

## Dependencies

- Python 3.x
- FastAPI
- Uvicorn
- SQLAlchemy
- Alembic
- psycopg2 (for PostgreSQL database)
- python-dotenv (for managing environment variables)
- Other dependencies (listed in `requirements.txt`)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/learning-platform.git
   cd learning-platform

2. Install dependencies:
`pip install -r requirements.txt´

3. Create a .env file in the project root and define the necessary environment variables, including DATABASE_URL for the database connection.

Example .env file:

`
DATABASE_URL=postgresql://username:password@localhost/learning_platform
REDIS_URL=redis://localhost
´

4. Create the initial database:
`python create_database.py´

5. Run database migrations:

`alembic upgrade head´

## Running the App Locally
Run the FastAPI application using Uvicorn:

`uvicorn app:app --reload´

Visit http://127.0.0.1:8000/docs in your browser to access the Swagger documentation.

Additional Notes
Adjust the database URL, Redis URL, and other settings in the .env file as needed.
Remember to update the database models and migration scripts as your application evolves.