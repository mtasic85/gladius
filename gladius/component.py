__all__ = [
    'Component',
    'ComponentLibrary',
]

import json
from uuid import uuid4
from copy import copy, deepcopy
from typing import Union, Self, Any

from .consts import EVENT_HANDLER_EVENT_TYPE_MAP
from .gladius import Gladius, Event

class Component:
    component_library: 'ComponentLibrary'
    attrs: dict
    data: str = ''
    children: list['Component']
    tag: str = 'div'
    default_class: str = ''
    default_attrs: dict[str, str] = {}

    # A void element is an element in HTML that cannot have any child nodes
    # (i.e., nested elements or text nodes).
    # Void elements only have a start tag;
    # end tags must not be specified for void elements.
    # https://developer.mozilla.org/en-US/docs/Glossary/Void_element
    void_element: bool = False
    
    def __init__(self, component_library: 'ComponentLibrary', data: str='', **kwargs):
        self.component_library = component_library
        
        # DOM attributes
        attrs = {**kwargs}

        if 'class' not in attrs and 'class_' not in attrs:
            attrs['class'] = self.default_class

        attrs['g-id'] = str(uuid4())
        self.attrs = {}
        self.set_attr(**attrs)

        # data
        # https://dom.spec.whatwg.org/#text
        self.data = data

        # children
        # https://dom.spec.whatwg.org/#ref-for-dom-parentnode-children
        self.children = []

    def set_attr(self, **kwargs) -> Self:
        # replace _ with -
        attrs = {
            k.replace('_', '-'): v
            for k, v in kwargs.items()
            if k not in ('class', 'class_', 'id', 'id_', 'content_', 'for_')
        }

        # class
        if 'class' in kwargs:
            attrs['class'] = kwargs['class']
        elif 'class_' in kwargs:
            attrs['class'] = kwargs['class_']

        # id
        if 'id' in kwargs:
            attrs['id'] = kwargs['id']
        elif 'id_' in kwargs:
            attrs['id'] = kwargs['id_']

        # for
        if 'for_' in kwargs:
            attrs['for'] = kwargs['for_']

        self.attrs.update(attrs)
        return self

    def get_attr(self, attr: str, default_value: str|None=None) -> Any:
        return self.attrs.get(attr, default_value)

    def del_attr(self, attr: str):
        del self.attrs[attr]

    def has_attr(self, attr: str) -> bool:
        return attr in self.attrs

    def add_class(self, class_: str) -> Self:
        component_class = self.attrs.get('class', '')
        class_ = component_class + ' ' + class_
        class_ = class_.strip()
        self.attrs['class'] = class_
        return self

    def remove_class(self, class_: str) -> Self:
        class_ = class_.strip()
        component_class = self.attrs.get('class', '')
        component_classes = [n for n in component_class.split() if n != class_]
        class_ = ' '.join(component_classes)
        self.attrs['class'] = class_
        return self

    def has_class(self, class_: str) -> bool:
        class_ = class_.strip()
        return class_ in self.attrs.get('class', '')

    def add(self, child: 'Component') -> Self:
        self.children.append(child)
        return self

    def remove(self, child: 'Component') -> Self:
        self.children.remove(child)
        return self

    def clone(self, deep: bool=True) -> Self:
        return deepcopy(self) if deep else copy(self)

    def _render_value(self, k, v) -> str:
        r: str

        if isinstance(v, str):
            r = json.dumps(v)
        else:
            r = f"'{json.dumps(v)}'"

        return r

    def _render_attr(self, k, v):
        attr: str
        g_id: str = self.attrs['g-id']

        if not k.startswith('_') and k in EVENT_HANDLER_EVENT_TYPE_MAP and callable(v):
            # standard events
            event_type: str = EVENT_HANDLER_EVENT_TYPE_MAP[k]

            attr = ' '.join([
                f'hx-trigger="{event_type}"',
                f'hx-post="/api/1.0/_event/{event_type}/{g_id}"',
                'hx-ext="json-enc,event-header"',
                'hx-swap="none"',
                'hx-headers=\'js:{"G-Session-ID": document.body.getAttribute("g-session-id")}\'',
            ])

            self.component_library.ctx.callbacks[g_id][event_type] = [self, v]
        elif k.startswith('_') and k in EVENT_HANDLER_EVENT_TYPE_MAP and callable(v):
            # custom events
            event_type: str = EVENT_HANDLER_EVENT_TYPE_MAP[k]

            attr = ' '.join([
                'hx-trigger="multi-path-deps"',
                f'hx-get="/api/1.0/_event/{event_type}/{g_id}"',
                'multi-path-deps=\'["/api/1.0/_event"]\'',
                f'hx-target=\'[g-id="{g_id}"]\'',
                'hx-swap="outerHTML"',
                'hx-headers=\'js:{"G-Session-ID": document.documentElement.getAttribute("g-session-id")}\'',
            ])

            self.component_library.ctx.callbacks[g_id][event_type] = [self, v]
        else:
            # other attrs - non-event/non-callback attrs
            attr = f'{k}={self._render_value(k, v)}'
        
        return attr

    def render_attrs(self) -> str:
        rendered_attrs: str = ' '.join(self._render_attr(k, v) for k, v in self.attrs.items())
        return rendered_attrs

    def render_children(self) -> str:
        rendered_children: str = '\n'.join(c.render() for c in self.children)
        return rendered_children

    def render(self) -> str:
        if self.void_element:
            return f'''
                <{self.tag} {self.render_attrs()} />
            '''
        else:
            return f'''
                <{self.tag} {self.render_attrs()}>
                    {self.data}
                    {self.render_children()}
                </{self.tag}>
            '''

class ComponentLibrary:
    ctx: Gladius
    component_map: dict[str, type]

    def __init__(self, ctx: Gladius):
        self.ctx = ctx

        component_map: dict[str, Component] = {
            k: v
            for k, v in dict(globals()).items()
            if isinstance(v, type) and issubclass(v, Component)
        }

        self.component_map = component_map

    def add_component_type(self, component_name: str, component_type: type):
        self.component_map[component_name] = component_type

    def get_component_type(self, component_name: str) -> type:
        return self.component_map[component_name]
