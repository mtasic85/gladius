__all__ = ['DaisyUI']

from .gladius import Gladius, EventRequest
from .component import Component, Div, ComponentLibrary

class Page(Component):
    default_class: str = 'container mx-auto'
    title: str

    def __init__(self, *args, title: str='Gladius', favicon: str='/static/gladius/favicon.png', **kwargs):
        super().__init__(*args, **kwargs)
        self.title = title
        self.favicon = favicon

    def render(self) -> str:
        rendered_children = '\n'.join(c.render() for c in self.children)

        return f'''
            <!doctype html>
            <html lang="en-US">
                <head>
                    <meta charset="utf-8" />
                    <meta name="viewport" content="width=device-width" />
                    <link rel="shortcut icon" type="image/png" href="{self.favicon}" />
                    <title>{self.title}</title>

                    <!-- daisyui -->
                    <link
                      href="https://cdn.jsdelivr.net/npm/daisyui@2.6.0/dist/full.css"
                      rel="stylesheet"
                      type="text/css"
                    />

                    <!-- tailwind -->
                    <script src="https://cdn.tailwindcss.com"></script>

                    <!-- htmx -->
                    <script src="https://unpkg.com/htmx.org@1.9.5"></script>
                    <script src="https://unpkg.com/htmx.org/dist/ext/debug.js"></script>
                    <script src="https://unpkg.com/htmx.org/dist/ext/json-enc.js"></script>
                    <script src="https://unpkg.com/htmx.org/dist/ext/event-header.js"></script>
                    <script src="/static/gladius/multi-path-deps.js"></script>
                </head>
                <body hx-ext='multi-path-deps'>
                    <div {self.render_props()}>
                        {rendered_children}
                    </div>
                </body>
            </html>
        '''

class Navbar(Component):
    default_class: str = 'navbar bg-base-100'

    def render(self) -> str:
        rendered_children = '\n'.join(c.render() for c in self.children)

        return f'''
            <div {self.render_props()}>
                {rendered_children}
            </div>
        '''

class Link(Component):
    default_class: str = 'btn btn-ghost normal-case text-xl'

    def render(self) -> str:
        rendered_children = '\n'.join(c.render() for c in self.children)

        return f'''
            <a {self.render_props()}>
                {rendered_children}
            </a>
        '''

class Flex(Div):
    default_class: str = 'flex w-full gap-1'

class VFlex(Div):
    default_class: str = 'flex flex-col w-full gap-1'

class Card(Div):
    default_class: str = 'grid h-20 flex-grow card bg-base-300 rounded-box place-items-center'

class Join(Div):
    default_class: str = 'join'

class VJoin(Div):
    default_class: str = 'join join-vertical'

class Button(Component):
    default_class: str = 'btn'

    def __init__(self, component_library: ComponentLibrary, **kwargs):
        super().__init__(component_library, **kwargs)

    def render(self) -> str:
        return f'''
            <button {self.render_props()}>
                {self.render_children()}
            </button>
        '''

class Table(Component):
    header: list[str]
    rows: list[list]

    def __init__(self, component_library: ComponentLibrary, header: list[str]=[], rows: list[list]=[], **kwargs):
        super().__init__(component_library, **kwargs)
        self.header = header
        self.rows = rows

        async def _ontablechange(table: Table, req: EventRequest):
            # print('_ontablechange', table, req)
            pass

        event_type: str = '_ontablechange'
        self.props[event_type] = _ontablechange

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
            <table class="table" {self.render_props()}>
                <thead>
                    {rendered_header}
                </thead>
                <tbody> 
                    {rendered_rows}
                </tbody>
            </table>
        '''

class DaisyUI(ComponentLibrary):
    def __init__(self, ctx: Gladius):
        super().__init__(ctx)

        component_map: dict[str, Component] = {
            k: v
            for k, v in dict(globals()).items()
            if isinstance(v, type) and issubclass(v, Component)
        }

        self.component_map = {**self.component_map, **component_map}

    def __getattr__(self, attr):
        ComponentType: type = self.get_component_type(attr)

        def _component(*args, **kwargs) -> Component:
            return ComponentType(self, *args, **kwargs)

        return _component
