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
    def __init__(self, component_library: ComponentLibrary, data: str='', **kwargs):
        super().__init__(component_library, role='button', data=data, **kwargs)

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
# forms
#
class Form(html5.Form): pass
class Label(html5.Label): pass
class Input(html5.Input): pass
class Select(html5.Select): pass
class Option(html5.Option): pass
class Fieldset(html5.Fieldset): pass
class Legend(html5.Legend): pass
class Text(html5.Text): pass

#
# tables
#
class Figure(html5.Figure): pass

class Table(html5.Table):
    header: list[str]
    rows: list[list]
    footer: list[str]

    def __init__(self, component_library: ComponentLibrary, header: list[str]=[], rows: list[list]=[], footer: list[str]=[], **kwargs):
        super().__init__(component_library, **kwargs)
        self.header = header
        self.rows = rows
        self.footer = footer

    def render(self) -> str:
        # render header
        rendered_header = None

        if self.header:
            rendered_header = '\n'.join([
                '<tr>',
                '\n'.join(f'<th>{h}</th>' for h in self.header),
                '</tr>',
            ])
        
        # render body
        rendered_rows = '\n'.join([
            '\n'.join([
                '<tr>',
                '\n'.join(f'<td>{v}</td>' for v in row),
                '</tr>',
            ]) for row in self.rows
        ])

        # render footer
        rendered_footer = None

        if self.footer:
            rendered_footer = '\n'.join([
                '<tr>',
                '\n'.join(f'<th>{h}</th>' for h in self.footer),
                '</tr>',
            ])

        # render table with header, body and footer
        rendered_component = f'<table class="table" {self.render_attrs()}>'

        if self.header:
            rendered_component += f'<thead> {rendered_header} </thead>'

        rendered_component += f'<tbody> {rendered_rows} </tbody>'

        if self.footer:
            rendered_component += f'<tfoot> {rendered_footer} </tfoot>'
        
        rendered_component += '</table>'
        return rendered_component

#
# accordions
#
class Details(html5.Details): pass
class Summary(html5.Summary): pass
class Ul(html5.Ul): pass
class Li(html5.Li): pass

#
# cards
#
class Article(html5.Article): pass
class Header(html5.Header): pass
class Footer(html5.Footer): pass

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
