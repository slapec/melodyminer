# coding: utf-8

from pathlib import Path

class SettingsModule:
    DATABASE_DSN: str
    WEB_HOST: str
    WEB_PORT: int
    MEDIA_DIR: Path


settings: SettingsModule
