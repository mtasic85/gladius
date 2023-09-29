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
    hello_card.data = f'Hello {v}'
    hello_button.data = f'Hello {v}'

async def world_button_click(button: Component, event: Event):
    v: int = randint(0, 100)
    world_card.data = f'World {v}'
    world_button.data = f'World {v}'

# html
html = h.Html()

# head
html.add(head := h.Head())
head.add(meta := h.Meta(charset='utf-8'))
head.add(meta := h.Meta(name='viewport', content='width=device-width'))
head.add(title := h.Title(data='Hello world 1'))
head.add(link := h.Link(rel='shortcut icon', type='image/png', href='/static/gladius/favicon.png'))
head.add(link := h.Link(href='https://cdn.jsdelivr.net/npm/daisyui@3.8.0/dist/full.css', rel='stylesheet', type='text/css'))
head.add(script := h.Script(src='https://cdn.tailwindcss.com?plugins=forms,typography,aspect-ratio'))
head.add(script := h.Script(src='https://unpkg.com/htmx.org@1.9.6'))
head.add(script := h.Script(src='https://unpkg.com/htmx.org/dist/ext/debug.js'))
head.add(script := h.Script(src='https://unpkg.com/htmx.org/dist/ext/json-enc.js'))
head.add(script := h.Script(src='https://unpkg.com/htmx.org/dist/ext/event-header.js'))
head.add(script := h.Script(src='/static/gladius/multi-path-deps.js'))

# body
html.add(body := h.Body(hx_ext='multi-path-deps').add_class('p-10'))
body.add(vflex := d.VFlex())

# cards
vflex.add(hello_card := d.Card('Hello'))
vflex.add(world_card := d.Card('World'))

# buttons
vflex.add(join := d.Join())
join.add(hello_button := d.Button('Hello', onclick=hello_button_click).add_class('btn-primary'))
join.add(world_button := d.Button('World', onclick=world_button_click).add_class('btn-secondary'))


# router
g.route('/', html)
app = g.get_app()

if __name__ == '__main__':
    g.run_app(host='0.0.0.0', port=5000)
