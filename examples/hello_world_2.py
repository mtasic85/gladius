from random import randint

from gladius import Gladius, Component, Event
from gladius.html5 import Html5
from gladius.daisyui import DaisyUI

g = Gladius()
h = Html5(g)
d = DaisyUI(g)

# callbacks
async def hello_button_click(button: Component, event: Event):
    v: int = randint(0, 100)
    hello_card.content = f'Hello {v}'
    hello_button.content = f'Hello {v}'

async def world_button_click(button: Component, event: Event):
    v: int = randint(0, 100)
    world_card.content = f'World {v}'
    world_button.content = f'World {v}'

page = h.Page()
page.head.add(title := h.Title(content='Hello world 1'))
page.head.add(link := h.Link(rel='shortcut icon', type='image/png', href='/static/gladius/favicon.png'))
page.head.add(link := h.Link(href='https://cdn.jsdelivr.net/npm/daisyui@3.8.0/dist/full.css', rel='stylesheet', type='text/css'))
page.head.add(script := h.Script(src='https://cdn.tailwindcss.com'))
page.head.add(script := h.Script(src='https://unpkg.com/htmx.org@1.9.6'))
page.head.add(script := h.Script(src='https://unpkg.com/htmx.org/dist/ext/debug.js'))
page.head.add(script := h.Script(src='https://unpkg.com/htmx.org/dist/ext/json-enc.js'))
page.head.add(script := h.Script(src='https://unpkg.com/htmx.org/dist/ext/event-header.js'))
page.head.add(script := h.Script(src='/static/gladius/multi-path-deps.js'))
page.body.set_attr(hx_ext='multi-path-deps').add_class('p-10')

# vflex
page.body.add(vflex := d.VFlex())

# cards
vflex.add(hello_card := d.Card('Hello'))
vflex.add(world_card := d.Card('World'))

# buttons
vflex.add(join := d.Join())
join.add(hello_button := d.Button('Hello', onclick=hello_button_click).add_class('btn-primary'))
join.add(world_button := d.Button('World', onclick=world_button_click).add_class('btn-secondary'))


# router
g.route('/', page)
app = g.get_app()

if __name__ == '__main__':
    g.run_app(host='0.0.0.0', port=5000)
