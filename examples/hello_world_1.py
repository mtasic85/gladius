from random import randint

from gladius import Gladius, Component, Event
from gladius.html5 import Html5
from gladius.daisyui import DaisyUI

g = Gladius()
html5 = Html5(g)
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

# html
html = html5.Html()

# head
html.add(head := html5.Head())
head.add(meta := html5.Meta(charset='utf-8'))
head.add(meta := html5.Meta(name='viewport', content='width=device-width'))
head.add(link := html5.Link(rel='shortcut icon', type='image/png', href='/static/gladius/favicon.png'))
head.add(title := html5.Title(content='Hello world 1'))
head.add(link := html5.Link(href='https://cdn.jsdelivr.net/npm/daisyui@3.7.7/dist/full.css', rel='stylesheet', type='text/css'))
head.add(script := html5.Script(src='https://cdn.tailwindcss.com'))
head.add(script := html5.Script(src='https://unpkg.com/htmx.org@1.9.5'))
head.add(script := html5.Script(src='https://unpkg.com/htmx.org/dist/ext/debug.js'))
head.add(script := html5.Script(src='https://unpkg.com/htmx.org/dist/ext/json-enc.js'))
head.add(script := html5.Script(src='https://unpkg.com/htmx.org/dist/ext/event-header.js'))
head.add(script := html5.Script(src='/static/gladius/multi-path-deps.js'))

# body
html.add(body := html5.Body(hx_ext='multi-path-deps').add_class('p-10'))
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
