__all__ = [
    'Html',
    'Head',
    'Meta',
    'Link',
    'Title',
    'Script',
    'Body',
    'Div',
    'Span',
    'Html5',
]

from .gladius import Gladius
from .component import Component, ComponentLibrary

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
    content: str

    def __init__(self, component_library: 'ComponentLibrary', content: str='', **kwargs):
        super().__init__(component_library, **kwargs)
        self.content = content

    def render(self) -> str:
        return f'''
            <{self.default_tag}> {self.content} </{self.default_tag}>
        '''

class Script(Component):
    default_tag: str = 'script'

class Body(Component):
    default_tag: str = 'body'

class A(Component):
    default_tag: str = 'a'

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
