# coding: utf-8

from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import INT8RANGE

from melodyminer import db


class Progress(db.Model):
    __tablename__ = 'marker_progress'

    media_id = sa.Column(
        None,
        sa.ForeignKey('media_audio.id'),
        primary_key=True
    )

    value = sa.Column(
        sa.BigInteger,
        nullable=False
    )

    created_at = sa.Column(
        sa.DateTime,
        nullable=False,
        default=datetime.now
    )

    updated_at = sa.Column(
        sa.DateTime,
        nullable=False
    )


class Bookmark(db.Model):
    __tablename__ = 'marker_bookmark'

    id = sa.Column(
        sa.Integer,
        primary_key=True
    )

    media_id = sa.Column(
        None,
        sa.ForeignKey('media_audio.id'),
        nullable=False
    )

    range = sa.Column(
        INT8RANGE,
        nullable=False
    )

    note = sa.Column(
        sa.String(512),
        nullable=True
    )

    created_at = sa.Column(
        sa.DateTime,
        nullable=False,
        default=datetime.now
    )
