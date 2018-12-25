# coding: utf-8

import logging

from aiohttp import web

from melodyminer import db, app

log = logging.getLogger(__name__)


async def setup(args):
    log.info('Connecting to the database')
    await db.set_bind('asyncpg://melodyminer:melodyminer@127.0.0.1:5432/melodyminer')

    log.info('Creating database scheme')
    await db.gino.create_all()

    log.info('Database has been created')


def start(args):
    app['config'] = {
        'gino': {
            'dsn': 'asyncpg://melodyminer:melodyminer@127.0.0.1:5432/melodyminer'
        }
    }

    db.init_app(app)

    return web.run_app(
        app=app,
        host=args.host,
        port=args.port
    )
