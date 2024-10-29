__all__ = [
    'Event',
    'Gladius',
]

import os
import asyncio
import inspect
from uuid import uuid4
from collections import defaultdict
from typing import TypedDict, Callable, Self

try:
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    pass

from aiohttp import web
from aiohttp.web import middleware
from aiohttp.web_urldispatcher import SystemRoute
from multidict import CIMultiDict

from .consts import EVENT_HANDLER_EVENT_TYPE_MAP

class Event(TypedDict, total=False):
    # Web event sent via htmx extenstion event-header
    # https://developer.mozilla.org/en-US/docs/Web/Events
    # https://htmx.org/extensions/event-header/
    pass

class Gladius:
    app: web.Application
    callbacks: dict[str, dict[str, tuple['Component', Callable]]] # {g_id: {event_type: [component, func]}}
    update_components: dict[str, list['Component']]

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

            # default aiohttp request handler
            excs = None

            try:
                response = await handler(request)
                return response
            except Exception as e:
                excs = [e]

            # gladius handler
            try:
                res: str | dict = await handler(self, req)
            except Exception as e:
                excs = [e]

            # if both throw error, 
            if excs:
                e = ExceptionGroup(f'request {request}, handler {handler} error', excs)
                raise e

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
            web.get('/api/1.0/_event/{event_type}/{g_id}', self.get_api_1_0__event),
            web.get('/api/1.0/_event/{event_type}/{g_session_id}/{g_id}', self.get_api_1_0__session_event),
            web.post('/api/1.0/_event/{event_type}/{g_id}', self.post_api_1_0__event),
        ])

        if os.path.exists('static'):
            self.app.add_routes([
                web.static('/static', 'static'),
            ])

        self.callbacks = defaultdict(dict)
        self.update_components = {}

    def add_route(self, method, path, handler):
        routes = [web.route(method.lower(), path, handler)]
        self.app.add_routes(routes)

    def route(self, path, component: 'Component'):
        async def _get_path_handler(request: web.Request) -> web.Response:
            # print('_get_path_handler:', request)
            res: str = component.render()
            response = web.Response(text=res, content_type='text/html')
            return response

        self.app.router.add_get(path, _get_path_handler)

    async def get_api_1_0__event(self, request: web.Request) -> web.Response:
        event_type: str = request.match_info['event_type']
        g_id: str = request.match_info['g_id']
        g_session_id: str = request.headers['G-Session-ID']
        # print('get_api_1_0__event:', request, event_type, g_id, g_session_id)
        
        component, callback = self.callbacks[g_id][event_type]
        await callback(component, {})
        
        res: str = component.render()
        # print('get_api_1_0__event:', res)
        response = web.Response(text=res, content_type='text/html')
        return response

    async def get_api_1_0__session_event(self, request: web.Request) -> web.Response:
        event_type: str = request.match_info['event_type']
        g_id: str = request.match_info['g_id']
        g_session_id: str = request.match_info['g_session_id']
        # print('get_api_1_0__session_event:', request, event_type, g_id, g_session_id)
        
        component, callback = self.callbacks[g_id][event_type]
        await callback(component, {})
        
        res: str = component.render()
        # print('get_api_1_0__session_event:', res)
        response = web.Response(text=res, content_type='text/html')
        return response

    async def post_api_1_0__event(self, request: web.Request) -> web.Response:
        event_type: str = request.match_info['event_type']
        g_id: str = request.match_info['g_id']
        g_session_id: str = request.headers['G-Session-ID']
        event: Event = request.headers['Triggering-Event']
        # print('post_api_1_0__event:', request, event_type, g_id, g_session_id, event)

        # self.update_components[g_session_id] = []
        component, callback = self.callbacks[g_id][event_type]
        res: dict = await callback(component, event)

        # print('post_api_1_0__event:', res)
        return web.json_response(res)

    def get_app(self):
        return self.app

    def run_app(self, *args, **kwargs):
        web.run_app(self.app, *args, **kwargs)
