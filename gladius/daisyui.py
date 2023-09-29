__all__ = [
    'Page',
    'Navbar',
    'NavbarButton',
    'Link',
    'Flex',
    'VFlex',
    'Card',
    'Join',
    'VJoin',
    'Button',
    'Table',
    'Text',
    'Artboard',
    'Divider',
    'Footer',
    'FooterTitle',
    'Hero',
    'HeroContent',
    'Indicator',
    'IndicatorItem',
    'Stack',
    'Toast',
    'Alert',
    'DaisyUI',
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
        self.head.add(link := h.Link(href='https://cdn.jsdelivr.net/npm/daisyui@3.8.0/dist/full.css', rel='stylesheet', type='text/css'))
        self.head.add(script := h.Script(src='https://cdn.tailwindcss.com'))

class Navbar(html5.Div):
    default_class: str = 'navbar bg-base-100'

    def add(self, child: Component) -> Self:
        child.set_attr(hx_target='body')
        self.children.append(child)
        return self

class NavbarButton(html5.A):
    # NOTE: extended component
    default_class: str = 'btn btn-ghost normal-case text-xl'

class Link(html5.A):
    default_class: str = 'link'

class Flex(html5.Div):
    default_class: str = 'flex w-full gap-1'

class VFlex(Flex):
    # NOTE: extended component
    default_class: str = 'flex flex-col w-full gap-1'

class Card(html5.Div):
    default_class: str = 'card grid h-20 flex-grow bg-base-300 rounded-box place-items-center'

class Join(html5.Div):
    default_class: str = 'join'

    def add(self, child: Component) -> Self:
        if not child.has_class('join-item'):
            child.add_class('join-item')
        
        child.set_attr(hx_target='body')
        self.children.append(child)
        return self

class VJoin(Join):
    # NOTE: extended component
    default_class: str = 'join join-vertical'

class Button(html5.Button):
    default_class: str = 'btn'

class Table(Component):
    header: list[str]
    rows: list[list]

    def __init__(self, component_library: ComponentLibrary, header: list[str]=[], rows: list[list]=[], **kwargs):
        super().__init__(component_library, **kwargs)
        self.header = header
        self.rows = rows

    def render(self) -> str:
        rendered_header = '\n'.join([
            '<tr>',
            '\n'.join(f'<th>{h}</th>' for h in self.header),
            '</tr>',
        ])
        
        rendered_rows = '\n'.join([
            '\n'.join([
                '<tr>',
                '\n'.join(f'<td>{v}</td>' for v in row),
                '</tr>',
            ]) for row in self.rows
        ])

        return f'''
            <table class="table" {self.render_attrs()}>
                <thead class="bg-base-200">
                    {rendered_header}
                </thead>
                <tbody> 
                    {rendered_rows}
                </tbody>
            </table>
        '''

class Text(html5.Text):
    pass

#
# Layout
#
class Artboard(html5.Div):
    default_class: str = 'artboard'

class Divider(html5.Div):
    default_class: str = 'divider'

# TODO: Drawer

class Footer(html5.Footer):
    default_class: str = 'footer'

class FooterTitle(html5.Header):
    # NOTE: extended component
    default_class: str = 'footer-title'

class Hero(html5.Div):
    default_class: str = 'hero bg-base-200'

class HeroContent(html5.Div):
    default_class: str = 'hero-content'

class Indicator(html5.Div):
    default_class: str = 'indicator'

class IndicatorItem(html5.Span):
    default_class: str = 'indicator-item'

# TODO: Mask

class Stack(html5.Div):
    default_class: str = 'stack'

class Toast(html5.Div):
    default_class: str = 'toast'

class Alert(html5.Div):
    default_class: str = 'alert'

#
# DaisyUI Component Library
#
class DaisyUI(ComponentLibrary):
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
