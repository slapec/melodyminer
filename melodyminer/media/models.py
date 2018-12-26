# coding: utf-8

from datetime import datetime
from pathlib import Path
from typing import TYPE_CHECKING, Optional

import sqlalchemy as sa

from melodyminer import db
from melodyminer.conf import settings

if TYPE_CHECKING:
    from melodyminer.marker.models import Progress


class Audio(db.Model):
    __tablename__ = 'media_audio'

    id = sa.Column(
        sa.String(32),
        primary_key=True,
        autoincrement=False
    )

    path = sa.Column(
        sa.String(512),
        nullable=False
    )

    title = sa.Column(
        sa.String(512),
        nullable=False
    )

    created_at = sa.Column(
        sa.DateTime,
        nullable=False,
        default=datetime.now
    )

    _progress: Optional['Progress'] = None

    @property
    def progress(self) -> Optional['Progress']:
        return self._progress

    @progress.setter
    def progress(self, value: 'Progress'):
        self._progress = value

    @property
    def absolute_path(self) -> Path:
        return settings.MEDIA_DIR / self.path
