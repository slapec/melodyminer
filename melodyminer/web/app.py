# coding: utf-8

import melodyminer.marker.views
import melodyminer.media.views
from aiohttp import web

app = web.Application()
app.add_routes([
    *melodyminer.media.views.routes,
    *melodyminer.marker.views.routes
])
