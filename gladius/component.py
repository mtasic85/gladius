__all__ = [
    'Component',
    'Div',
    'Text',
    'ComponentLibrary',
]

import json
from uuid import uuid4
from typing import Union

from .consts import EVENT_HANDLER_EVENT_TYPE_MAP

class Component:
    component_library: 'ComponentLibrary'
    props: dict
    children: list['Component']
    default_class: str = ''
    
    def __init__(self, component_library: 'ComponentLibrary', **kwargs):
        self.component_library = component_library
        
        # props
        if 'class' in kwargs:
            class_ = kwargs['class']
        elif 'class_' in kwargs:
            class_ = kwargs['class_']
        else:
            class_ = self.default_class

        id_ = ''
        id_ += kwargs.get('id', '')
        id_ += kwargs.get('id_', '')

        props = {
            k.replace('_', '-'): v
            for k, v in kwargs.items()
            if k not in ('class', 'class_', 'id', 'id_')
        }

        self.props = {}
        
        if class_:
            self.props['class'] = class_

        if id_:
            self.props['id'] = id_

        # FIXME: requires sf_session
        self.props['sf_id'] = str(uuid4())
        self.props.update(props)

        # children
        self.children = []

    def add(self, child: Union['Component', str]) -> 'Component':
        if isinstance(child, str):
            child = Text(component_library=self.component_library, content=child)

        self.children.append(child)
        return self

    def _render_value(self, k, v) -> str:
        r: str

        if isinstance(v, str):
            r = json.dumps(v)
        else:
            r = f"'{json.dumps(v)}'"

        return r

    def _render_prop(self, k, v):
        prop: str

        if k == 'onclick' and callable(v):
            sf_id: str = self.props['sf_id']
            event_type: str = EVENT_HANDLER_EVENT_TYPE_MAP[k]

            prop = ' '.join([
                'hx-trigger="click"',
                f'hx-post="/api/1.0/_event/{event_type}/{sf_id}"',
                'hx-ext="json-enc,event-header"',
                'hx-swap="none"',
            ])

            self.component_library.ctx.callbacks[sf_id][event_type] = [self, v]
        elif k == '_ontablechange' and callable(v):
            sf_id: str = self.props['sf_id']
            event_type: str = EVENT_HANDLER_EVENT_TYPE_MAP[k]

            prop = ' '.join([
                f'id="table-{sf_id}"',
                f'hx-get="/api/1.0/_event/{event_type}/{sf_id}"',
                'hx-trigger="multi-path-deps"',
                'multi-path-deps=\'["/api/1.0/_event"]\'',
                f'hx-target="#table-{sf_id}"',
                'hx-swap="outerHTML"',
            ])

            self.component_library.ctx.callbacks[sf_id][event_type] = [self, v]
        elif k == '_ontextchange' and callable(v):
            sf_id: str = self.props['sf_id']
            event_type: str = EVENT_HANDLER_EVENT_TYPE_MAP[k]

            prop = ' '.join([
                f'id="table-{sf_id}"',
                f'hx-get="/api/1.0/_event/{event_type}/{sf_id}"',
                'hx-trigger="multi-path-deps"',
                'multi-path-deps=\'["/api/1.0/_event"]\'',
                f'hx-target="#table-{sf_id}"',
                'hx-swap="outerHTML"',
            ])

            self.component_library.ctx.callbacks[sf_id][event_type] = [self, v]
        else:
            prop = f'{k}={self._render_value(k, v)}'
        
        return prop

    def render_props(self) -> str:
        rendered_props: str = ' '.join(self._render_prop(k, v) for k, v in self.props.items())
        return rendered_props

    def render_children(self) -> str:
        rendered_children: str = '\n'.join(c.render() for c in self.children)
        return rendered_children

    def render(self) -> str:
        raise NotImplemented

class Div(Component):
    def render(self) -> str:
        return f'''
            <div {self.render_props()}>
                {self.render_children()}
            </div>
        '''

class Span(Component):
    def render(self) -> str:
        return f'''
            <span {self.render_props()}>
                {self.render_children()}
            </span>
        '''

class Text(Component):
    content: str

    def __init__(self, component_library: 'ComponentLibrary', content: str='', **kwargs):
        super().__init__(component_library, **kwargs)
        self.content = content

        async def _ontextchange(text: Text, req: 'EventRequest'):
            # print('_ontextchange', text, req)
            pass

        event_type: str = '_ontextchange'
        self.props[event_type] = _ontextchange

    def render(self) -> str:
        return f'''
            <span {self.render_props()}>
                {self.content}
            </span>
        '''

class ComponentLibrary:
    ctx: 'Gladius'
    component_map: dict[str, type]

    def __init__(self, ctx: 'Gladius'):
        self.ctx = ctx

        component_map: dict[str, Component] = {
            k: v for k, v in dict(globals()).items() if isinstance(v, type) and issubclass(v, Component)
        }

        self.component_map = component_map

    def add_component_type(self, component_name: str, component_type: type):
        self.component_map[component_name] = component_type

    def get_component_type(self, component_name: str) -> type:
        return self.component_map[component_name]