from random import randint

from gladius import Gladius, Component, EventRequest
from gladius.html5 import Html5
from gladius.daisyui import DaisyUI

# glados daisyui
g = Gladius()
html5 = Html5(g)
d = DaisyUI(g)

# callbacks
async def hello_button_click(button: Component, req: EventRequest):
    hello_text.content = f'Hello {randint(0, 100)}'

async def world_button_click(button: Component, req: EventRequest):
    world_text.content = f'World {randint(0, 100)}'

# html
html = html5.Html()

# head
html.add(head := html5.Head())
head.add(meta := html5.Meta(charset='utf-8'))
head.add(meta := html5.Meta(name='viewport', content='width=device-width'))
head.add(link := html5.Link(rel='shortcut icon', type='image/png', href='/static/gladius/favicon.png'))
head.add(title := html5.Title(content='Hello world 1'))
head.add(link := html5.Link(href='https://cdn.jsdelivr.net/npm/daisyui@2.6.0/dist/full.css', rel='stylesheet', type='text/css'))
head.add(script := html5.Script(src='https://cdn.tailwindcss.com'))
head.add(script := html5.Script(src='https://unpkg.com/htmx.org@1.9.5'))
head.add(script := html5.Script(src='https://unpkg.com/htmx.org/dist/ext/debug.js'))
head.add(script := html5.Script(src='https://unpkg.com/htmx.org/dist/ext/json-enc.js'))
head.add(script := html5.Script(src='https://unpkg.com/htmx.org/dist/ext/event-header.js'))
head.add(script := html5.Script(src='/static/gladius/multi-path-deps.js'))

# body
html.add(body := html5.Body(hx_ext='multi-path-deps'))
body.add(vflex := d.VFlex())

# top cards
vflex.add(card := d.Card())
card.add(hello_text := d.Text('Hello'))

vflex.add(card := d.Card())
card.add(world_text := d.Text('World'))

# buttons
vflex.add(hflex := d.Flex())
hflex.add(join := d.Join())
join.add(button := d.Button(class_='btn btn-primary', onclick=hello_button_click))
button.add(text := d.Text('Hello'))
join.add(button := d.Button(class_='btn btn-success', onclick=world_button_click))
button.add(text := d.Text('World'))

# router
g.route('/', html)
app = g.get_app()

if __name__ == '__main__':
    g.run_app(host='0.0.0.0', port=5000)
