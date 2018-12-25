# coding: utf-8

from typing import List

from aiohttp import web

from melodyminer.media.models import Audio

routes = web.RouteTableDef()


@routes.get('/media/audio', name='media:audio-list')
async def audio_list(request: web.Request):
    audio_models: List[Audio] = await Audio.query.gino.all()

    media = []
    for audio in audio_models:
        media.append({
            'id': audio.id,
            'title': audio.title,
            'created_at': audio.created_at.isoformat()
        })

    return web.json_response({
        'media': media
    })
