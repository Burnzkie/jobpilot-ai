import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DATABASE_URL: str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    ALGORITHM: str

    MAX_UPLOAD_SIZE: int = 5 * 1024 * 1024

    ALLOWED_UPLOAD_EXTENSIONS: list[str] = [
        ".pdf",
        ".docx",
    ]

    ALLOWED_CONTENT_TYPES: list[str] = [
        "application/pdf",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    ]

    RESUME_UPLOAD_DIR: str = "uploads/resumes"
    TESTING: bool = False

    model_config = SettingsConfigDict(
        env_file=os.getenv("ENV_FILE", ".env"), extra="ignore"
    )


settings = Settings()
