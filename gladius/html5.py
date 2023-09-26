__all__ = [
    'Page',
    'Html',
    'Head',
    'Meta',
    'Link',
    'Title',
    'Script',
    'Body',
    'Div',
    'Span',
    'Footer',
    'Nav',
    'Header',
    'H1',
    'H2',
    'H3',
    'H4',
    'P',
    'A',
    'BlockQuote',
    'Figure',
    'FigCaption',
    'Strong',
    'Em',
    'Code',
    'Pre',
    'Ol',
    'Ul',
    'Li',
    'Table',
    'THead',
    'Tr',
    'Th',
    'Td',
    'Img',
    'Video',
    'Source',
    'Hr',
    'Button',
    'Html5',
]

from typing import Self

from .gladius import Gladius
from .component import Component, ComponentLibrary

class Page(Component):
    # NOTE: high-level component
    default_tag: str = 'html'
    title: str
    favicon: str
    html: 'Html'
    head: 'Head'
    body: 'Body'

    def __init__(self, component_library: 'ComponentLibrary', title: str='Gladius', favicon: str='/static/gladius/favicon.png', **kwargs):
        super().__init__(component_library, **kwargs)
        self.title = title
        self.favicon = favicon
        h: ComponentLibrary = Html5(component_library.ctx)

        # html
        html = h.Html()
        self.html = html
        
        # head
        html.add(head := h.Head())
        head.add(meta := h.Meta(charset='utf-8'))
        head.add(meta := h.Meta(name='viewport', content='width=device-width'))
        head.add(title := h.Title(content=self.title))
        head.add(link := h.Link(rel='shortcut icon', type='image/png', href=self.favicon))
        self.head = head

        # body
        html.add(body := h.Body())
        self.body = body

    def add(self, child: 'Component') -> Self:
        self.body.children.append(child)
        return self

    def render(self) -> str:
        return self.html.render()

class Html(Component):
    default_tag: str = 'html'
    default_attrs: dict = {'lang': 'en-US'}

    def render(self) -> str:
        return f'''
            <!doctype html>
            <{self.default_tag} {self.render_attrs()}>
                {self.render_children()}
            </{self.default_tag}>
        '''

class Head(Component):
    default_tag: str = 'head'

class Meta(Component):
    default_tag: str = 'meta'
    void_element: bool = True

class Link(Component):
    default_tag: str = 'link'
    void_element: bool = True

class Title(Component):
    default_tag: str = 'title'

class Script(Component):
    default_tag: str = 'script'

class Body(Component):
    default_tag: str = 'body'

class Div(Component):
    default_tag: str = 'div'

class Span(Component):
    default_tag: str = 'span'

class Footer(Component):
    default_tag: str = 'footer'

class Nav(Component):
    default_tag: str = 'nav'

class Header(Component):
    default_tag: str = 'header'

class H1(Component):
    default_tag: str = 'h1'

class H2(Component):
    default_tag: str = 'h2'

class H3(Component):
    default_tag: str = 'h3'

class H4(Component):
    default_tag: str = 'h4'

class P(Component):
    default_tag: str = 'p'

class A(Component):
    default_tag: str = 'a'

class BlockQuote(Component):
    default_tag: str = 'blockquote'

class Figure(Component):
    default_tag: str = 'figure'

class FigCaption(Component):
    default_tag: str = 'figcaption'

class Strong(Component):
    default_tag: str = 'strong'

class Em(Component):
    default_tag: str = 'em'

class Code(Component):
    default_tag: str = 'code'

class Pre(Component):
    default_tag: str = 'pre'

class Ol(Component):
    default_tag: str = 'ol'

class Ul(Component):
    default_tag: str = 'ul'

class Li(Component):
    default_tag: str = 'li'

class Table(Component):
    default_tag: str = 'table'

class THead(Component):
    default_tag: str = 'thead'

class Tr(Component):
    default_tag: str = 'tr'

class Th(Component):
    default_tag: str = 'th'

class Td(Component):
    default_tag: str = 'td'

class Img(Component):
    default_tag: str = 'img'
    void_element: bool = True

class Video(Component):
    default_tag: str = 'video'

class Source(Component):
    default_tag: str = 'source'
    void_element: bool = True

class Hr(Component):
    default_tag: str = 'hr'
    void_element: bool = True

class Button(Component):
    default_tag: str = 'button'

class Html5(ComponentLibrary):
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
