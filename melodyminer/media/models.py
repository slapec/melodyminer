# coding: utf-8

from datetime import datetime

import sqlalchemy as sa

from melodyminer import db


class Audio(db.Model):
    __tablename__ = 'media_audio'

    id = sa.Column(
        sa.Integer,
        primary_key=True
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
