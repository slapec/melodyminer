# coding: utf-8

from pathlib import Path

WEB_HOST = '0.0.0.0'
WEB_PORT = 9001
DATABASE_DSN = 'asyncpg://melodyminer:melodyminer@127.0.0.1:5432/melodyminer'
MEDIA_DIR = Path(__file__).parent / 'media'

MEDIA_DIR.mkdir(parents=True, exist_ok=True)
