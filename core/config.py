# config.py
import os
from dotenv import load_dotenv
from pathlib import Path
env_path = Path('.') / ".env"


class Settings:
    PROJECT_NAME: str = "Job Board"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER : str = 'postgres'
    POSTGRES_PASSWORD : str = '1969'
    POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT : str = os.getenv("POSTGRES_PORT", 5433)
    POSTGRES_DB : str = os.getenv("POSTGRES_DB", "fastapitest")
    # DATABASE_URL = "jdbc:postgresql://localhost:5433/postgres"
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


settings = Settings()
