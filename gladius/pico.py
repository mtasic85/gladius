__all__ = [
    'Page',
    'Main',
    'Grid',
    'Headings',
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

#
# layout
#
class Main(html5.Main):
    default_class: str = 'container'

class Grid(html5.Div):
    default_class: str = 'grid'

class Div(html5.Div):
    pass

#
# typography
#
class H1(html5.H1): pass
class H2(html5.H2): pass
class H3(html5.H3): pass
class H4(html5.H4): pass
class H5(html5.H5): pass
class H6(html5.H6): pass
class HGroup(html5.HGroup): pass

class Headings(html5.Div):
    default_class: str = 'headings'

class P(html5.P): pass
class Abbr(html5.Abbr): pass
class Strong(html5.Strong): pass
class B(html5.B): pass
class I(html5.I): pass
class Em(html5.Em): pass
class Cite(html5.Cite): pass
class Del(html5.Del): pass
class Ins(html5.Ins): pass
class Kbd(html5.Kbd): pass
class Mark(html5.Mark): pass
class S(html5.S): pass
class Small(html5.Small): pass
class Sub(html5.Sub): pass
class Sup(html5.Sup): pass
class U(html5.U): pass
class Link(html5.A): pass

class SecondaryLink(Link):
    default_class: str = 'secondary'

class ContrastLink(Link):
    default_class: str = 'contrast'

class BlockQuote(html5.BlockQuote): pass
class Footer(html5.Footer): pass

#
# buttons
#
class Button(html5.Button): pass

class SubmitInput(html5.Input):
    def __init__(self, component_library: ComponentLibrary, **kwargs):
        super().__init__(component_library, type='submit', **kwargs)

class ButtonLink(html5.A):
    def __init__(self, component_library: ComponentLibrary, content: str='', **kwargs):
        super().__init__(component_library, role='button', content=content, **kwargs)

class SecondaryButtonLink(ButtonLink):
    default_class: str = 'secondary'

class ContrastButtonLink(ButtonLink):
    default_class: str = 'contrast'

class OutlineButtonLink(ButtonLink):
    default_class: str = 'outline'

class SecondaryOutlineButtonLink(ButtonLink):
    default_class: str = 'secondary outline'

class ContrastOutlineButtonLink(ButtonLink):
    default_class: str = 'contrast outline'

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
