# coding: utf-8

import logging

from aiohttp import web

from melodyminer import db, app
from melodyminer.conf import settings

log = logging.getLogger(__name__)


async def setup(args):
    log.info('Creating database scheme')
    await db.gino.create_all()

    log.info('Database has been created')


def start(args):
    app['config'] = {
        'gino': {
            'dsn': settings.DATABASE_DSN
        }
    }

    db.init_app(app)

    return web.run_app(
        app=app,
        host=settings.WEB_HOST,
        port=settings.WEB_PORT
    )
