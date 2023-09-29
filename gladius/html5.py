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
    'Main',
    'HGroup',
    'Abbr',
    'B',
    'I',
    'Cite',
    'Del',
    'Ins',
    'Kbd',
    'Mark',
    'S',
    'Small',
    'Sub',
    'Sup',
    'U',
    'Input',
    'Form',
    'Label',
    'Select',
    'Option',
    'Fieldset',
    'Legend',
    'Text',
    'Table',
    'THead',
    'TR',
    'TH',
    'TBody',
    'TD',
    'TFoot',
    'Details',
    'Summary',
    'Article',
    'Html5',
]

from uuid import uuid4
from typing import Self

from .gladius import Gladius, Event
from .component import Component, ComponentLibrary

class Page(Component):
    # NOTE: high-level component
    tag: str = 'html'
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
        head.add(title := h.Title(data=self.title))
        head.add(link := h.Link(rel='shortcut icon', type='image/png', href=self.favicon))
        head.add(script := h.Script(src='https://unpkg.com/htmx.org@1.9.6'))
        head.add(script := h.Script(src='https://unpkg.com/htmx.org/dist/ext/debug.js'))
        head.add(script := h.Script(src='https://unpkg.com/htmx.org/dist/ext/json-enc.js'))
        head.add(script := h.Script(src='https://unpkg.com/htmx.org/dist/ext/event-header.js'))
        head.add(script := h.Script(src='https://unpkg.com/idiomorph/dist/idiomorph-ext.min.js'))
        head.add(script := h.Script(src='/static/gladius/multi-path-deps.js'))
        self.head = head

        # body
        html.add(body := h.Body(hx_ext='multi-path-deps,morph', hx_boost='true', hx_swap='morph:innerHTML'))
        self.body = body

    def add(self, child: 'Component') -> Self:
        self.body.children.append(child)
        return self

    def render(self) -> str:
        # create new g_session_id for each GET request
        g_session_id = str(uuid4())
        self.html.set_attr(g_session_id=g_session_id)
        return self.html.render()

class Html(Component):
    tag: str = 'html'
    default_attrs: dict = {'lang': 'en-US'}

    def render(self) -> str:
        return f'''
            <!doctype html>
            <{self.tag} {self.render_attrs()}>
                {self.render_children()}
            </{self.tag}>
        '''

class Head(Component):
    tag: str = 'head'

class Meta(Component):
    tag: str = 'meta'
    void_element: bool = True

class Link(Component):
    tag: str = 'link'
    void_element: bool = True

class Title(Component):
    tag: str = 'title'

class Script(Component):
    tag: str = 'script'

class Body(Component):
    tag: str = 'body'

    def __init__(self, component_library: 'ComponentLibrary', **kwargs):
        super().__init__(component_library, **kwargs)

        # content change
        async def _oncontentchange(content: str, event: Event):
            # print('_oncontentchange', content, event)
            pass

        event_type: str = '_oncontentchange'
        self.attrs[event_type] = _oncontentchange

class Div(Component):
    tag: str = 'div'

class Span(Component):
    tag: str = 'span'

class Footer(Component):
    tag: str = 'footer'

class Nav(Component):
    tag: str = 'nav'

class Header(Component):
    tag: str = 'header'

class H1(Component):
    tag: str = 'h1'

class H2(Component):
    tag: str = 'h2'

class H3(Component):
    tag: str = 'h3'

class H4(Component):
    tag: str = 'h4'

class H5(Component):
    tag: str = 'h5'

class H6(Component):
    tag: str = 'h6'

class P(Component):
    tag: str = 'p'

class A(Component):
    tag: str = 'a'

class BlockQuote(Component):
    tag: str = 'blockquote'

class Figure(Component):
    tag: str = 'figure'

class FigCaption(Component):
    tag: str = 'figcaption'

class Strong(Component):
    tag: str = 'strong'

class Em(Component):
    tag: str = 'em'

class Code(Component):
    tag: str = 'code'

class Pre(Component):
    tag: str = 'pre'

class Ol(Component):
    tag: str = 'ol'

class Ul(Component):
    tag: str = 'ul'

class Li(Component):
    tag: str = 'li'

class Table(Component):
    tag: str = 'table'

class THead(Component):
    tag: str = 'thead'

class Tr(Component):
    tag: str = 'tr'

class Th(Component):
    tag: str = 'th'

class Td(Component):
    tag: str = 'td'

class Img(Component):
    tag: str = 'img'
    void_element: bool = True

class Video(Component):
    tag: str = 'video'

class Source(Component):
    tag: str = 'source'
    void_element: bool = True

class Hr(Component):
    tag: str = 'hr'
    void_element: bool = True

class Button(Component):
    tag: str = 'button'

class Main(Component):
    tag: str = 'main'

class HGroup(Component):
    tag: str = 'hgroup'

class Abbr(Component):
    tag: str = 'abbr'

class B(Component):
    tag: str = 'b'

class I(Component):
    tag: str = 'I'

class Cite(Component):
    tag: str = 'cite'

class Del(Component):
    tag: str = 'del'

class Ins(Component):
    tag: str = 'ins'

class Kbd(Component):
    tag: str = 'kbd'

class Mark(Component):
    tag: str = 'mark'

class S(Component):
    tag: str = 's'

class Small(Component):
    tag: str = 'small'

class Sub(Component):
    tag: str = 'sub'

class Sup(Component):
    tag: str = 'sup'

class U(Component):
    tag: str = 'u'

class Input(Component):
    tag: str = 'input'
    void_element: bool = True

class Form(Component):
    tag: str = 'form'

class Label(Component):
    tag: str = 'label'

class Select(Component):
    tag: str = 'select'

class Option(Component):
    tag: str = 'option'

class Fieldset(Component):
    tag: str = 'fieldset'

class Legend(Component):
    tag: str = 'legend'

class Text(Span):
    # NOTE: extended component
    pass

class Table(Component):
    tag: str = 'table'

class THead(Component):
    tag: str = 'thead'

class TR(Component):
    tag: str = 'tr'

class TH(Component):
    tag: str = 'th'

class TBody(Component):
    tag: str = 'tbody'

class TD(Component):
    tag: str = 'td'

class TFoot(Component):
    tag: str = 'tfoot'

class Details(Component):
    tag: str = 'details'

class Summary(Component):
    tag: str = 'summary'

class Article(Component):
    tag: str = 'article'

#
# Html5 Component Library
#
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
