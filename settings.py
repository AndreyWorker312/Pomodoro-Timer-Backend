from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    sqlite_db_name: str = "postgresql+psycopg2://postgres:password@0.0.0.0:5432/pomodoro"