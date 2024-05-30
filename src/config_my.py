import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_USER = os.getenv("DB_USER")

if not all([DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER]):
    raise EnvironmentError('One or more environment variables are missing.')
