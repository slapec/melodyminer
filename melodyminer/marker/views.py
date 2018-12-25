# coding: utf-8

from aiohttp import web

routes = web.RouteTableDef()


@routes.get('/markers', name='markers')
async def hello(request: web.Request):
    return web.Response(text='Hello World')
