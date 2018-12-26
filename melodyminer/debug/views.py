# coding: utf-8

import logging

from aiohttp import web
from aiohttp_sse import sse_response

routes = web.RouteTableDef()


@routes.get('/debug/log-stream')
async def log_stream(request: web.Request):
    async with sse_response(request) as resp:
        await resp.send('WIP')

    return resp
