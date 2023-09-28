__all__ = [
    'Page',
    'Main',
    'Grid',
    'Pico',
]

from typing import Self

from .gladius import Gladius, Event
from .component import Component, ComponentLibrary
from . import html5

class Page(html5.Page):
    # NOTE: high-level component
    default_class: str = 'container mx-auto'

    def __init__(self, component_library: ComponentLibrary, **kwargs):
        super().__init__(component_library, **kwargs)
        h: ComponentLibrary = html5.Html5(component_library.ctx)
        self.head.add(link := h.Link(href='https://cdn.jsdelivr.net/npm/@picocss/pico@1/css/pico.min.css', rel='stylesheet', type='text/css'))

class Main(html5.Main):
    default_class: str = 'container'

class Grid(html5.Div):
    default_class: str = 'grid'

#
# Pico Component Library
#
class Pico(ComponentLibrary):
    def __init__(self, ctx: Gladius):
        super().__init__(ctx)

        self.component_map: dict[str, Component] = {
            k: v
            for k, v in dict(globals()).items()
            if isinstance(v, type) and issubclass(v, Component)
        }

    def __getattr__(self, attr):
        ComponentType: type = self.get_component_type(attr)

        def _component(*args, **kwargs) -> Component:
            return ComponentType(self, *args, **kwargs)

        return _component
