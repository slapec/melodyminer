# coding: utf-8

from aiohttp import web

import melodyminer.marker.views
import melodyminer.media.views
from melodyminer import db

app = web.Application(middlewares=(
    db,
))

app.add_routes([
    *melodyminer.media.views.routes,
    *melodyminer.marker.views.routes
])
