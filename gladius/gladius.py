__all__ = [
    'Event',
    'Gladius',
]

import os
import asyncio
import inspect
from collections import defaultdict
from typing import TypedDict, Callable

try:
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    pass

from aiohttp import web
from aiohttp.web import middleware
from aiohttp.web_urldispatcher import SystemRoute

from .consts import EVENT_HANDLER_EVENT_TYPE_MAP

class Event(TypedDict, total=False):
    sf_id: str
    # type: str
    # ...

class Gladius:
    app: web.Application
    callbacks: dict[str, dict[str, tuple['Component', Callable]]] # {sf_id: {event_type: [component, func]}}

    def __init__(self):
        @middleware
        async def gladius_middleware(request: web.Request, handler: Callable) -> web.Response:
            # print(request, handler)
            req: dict

            if request.method == 'GET':
                req = dict(request.query)
            else:
                req = await request.json()

            response: web.Response

            # TODO: check line below for better request handling
            # if inspect.ismethod(handler) and hasattr(handler, '__self__') and isinstance(handler.__self__, SystemRoute):
            if inspect.ismethod(handler):
                response = await handler(request)
                return response

            res: str | dict = await handler(self, req)

            if isinstance(res, str):
                response = web.Response(text=res, content_type='text/html')
            elif isinstance(res, dict):
                response = web.json_reponse(res)
            else:
                raise ValueError(res)

            return response

        self.app = web.Application(middlewares=[gladius_middleware])
        
        self.app.add_routes([
            web.static('/static/gladius', os.path.join(os.path.split(__loader__.path)[0], 'static')),
            web.get('/api/1.0/_event/{event_type}/{sf_id}', self.get_api_1_0__event),
            web.post('/api/1.0/_event/{event_type}/{sf_id}', self.post_api_1_0__event),
        ])

        if os.path.exists('static'):
            self.app.add_routes([
                web.static('/static', 'static'),
            ])

        self.callbacks = defaultdict(dict)

    def add_route(self, method, path, handler):
        routes = [web.route(method.lower(), path, handler)]
        self.app.add_routes(routes)

    def route(self, path, component: 'Component'):
        async def _handler(sf, req) -> str:
            rendered_component: str = component.render()
            return rendered_component

        self.app.router.add_get(path, _handler)

    async def get_api_1_0__event(self, request: web.Request) -> web.Response:
        event_type: str = request.match_info['event_type']
        sf_id: str = request.match_info['sf_id']
        # print('get_api_1_0__event:', event_type, sf_id)
        component, callback = self.callbacks[sf_id][event_type]
        await callback(component, {})
        res: str = component.render()
        # print('get_api_1_0__event:', res)
        return web.Response(text=res, content_type='text/html')

    async def post_api_1_0__event(self, request: web.Request) -> web.Response:
        event_type: str = request.match_info['event_type']
        sf_id: str = request.match_info['sf_id']
        event: Event = request.headers['Triggering-Event']
        # print('post_api_1_0__event:', event_type, sf_id, event)
        component, callback = self.callbacks[sf_id][event_type]
        res: dict = await callback(component, event)
        # print('post_api_1_0__event:', res)
        return web.json_response(res)

    def get_app(self):
        return self.app

    def run_app(self, *args, **kwargs):
        web.run_app(self.app, *args, **kwargs)
