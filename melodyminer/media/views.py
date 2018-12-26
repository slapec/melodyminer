# coding: utf-8

from typing import List

from aiohttp import web

from melodyminer.marker.models import Progress
from melodyminer.media.models import Audio

routes = web.RouteTableDef()


@routes.get('/api/v1/media/audio/', name='media:audio-list')
async def audio_list(request: web.Request):
    route = request.app.router['media:audio-stream']

    audio_models: List[Audio] = await Audio.load(progress=Progress).order_by(Audio.created_at.desc()).gino.all()

    media = []
    for audio in audio_models:
        media.append({
            'id': audio.id,
            'title': audio.title,
            'created_at': audio.created_at.isoformat(),
            'progress': getattr(audio.progress, 'value', None),
            'url': str(route.url_for(id=audio.id))
        })

    return web.json_response(media)


@routes.get('/api/v1/media/audio/{id:[a-f0-9]{32}}/stream', name='media:audio-stream')
async def audio_stream(request: web.Request):
    audio: Audio = await Audio.get_or_404(request.match_info.get('id'))

    return web.FileResponse(audio.path)
