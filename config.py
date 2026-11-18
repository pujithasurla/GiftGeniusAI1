"""Application configuration loaded from environment variables."""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")


class Config:
    """Base Flask configuration for GiftGenius AI."""

    APP_NAME: str = os.getenv("APP_NAME", "GiftGenius AI")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "dev-only-insecure-key")
    DEBUG: bool = os.getenv("FLASK_DEBUG", "False").lower() in {"1", "true", "yes"}

    # Ollama
    OLLAMA_BASE_URL: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434").rstrip("/")
    OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "llama3")
    OLLAMA_TIMEOUT: int = int(os.getenv("OLLAMA_TIMEOUT", "120"))

    # Database
    SQLALCHEMY_DATABASE_URI: str = os.getenv(
        "DATABASE_URL",
        f"sqlite:///{BASE_DIR / 'instance' / 'giftgenius.db'}",
    )
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False

    # Paths
    BASE_DIR: Path = BASE_DIR
    REPORTS_DIR: Path = BASE_DIR / "reports"
    STATIC_DIR: Path = BASE_DIR / "static"
    LOG_DIR: Path = BASE_DIR / "logs"
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO").upper()

    # Session
    SESSION_COOKIE_HTTPONLY: bool = True
    SESSION_COOKIE_SAMESITE: str = "Lax"
    PERMANENT_SESSION_LIFETIME: int = 60 * 60 * 24 * 7  # 7 days


class DevelopmentConfig(Config):
    """Development configuration."""

    DEBUG = True


class ProductionConfig(Config):
    """Production configuration."""

    DEBUG = False
    SESSION_COOKIE_SECURE: bool = True


def get_config(env: str | None = None) -> type[Config]:
    """Return the config class for the given Flask environment name."""
    environment = (env or os.getenv("FLASK_ENV", "development")).lower()
    mapping: dict[str, type[Config]] = {
        "development": DevelopmentConfig,
        "production": ProductionConfig,
        "default": DevelopmentConfig,
    }
    return mapping.get(environment, DevelopmentConfig)
