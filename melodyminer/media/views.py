# coding: utf-8

from aiohttp import web

routes = web.RouteTableDef()


@routes.get('/media', name='media')
async def hello(request: web.Request):
    return web.json_response({
        'media': []
    })
