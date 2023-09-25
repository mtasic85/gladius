from random import randint

from gladius import Gladius, Component, EventRequest
from gladius.daisyui import DaisyUI

# glados daisyui
g = Gladius()
d = DaisyUI(g)

# callbacks
async def hello_button_click(button: Component, req: EventRequest):
    hello_text.content = f'Hello {randint(0, 100)}'

async def world_button_click(button: Component, req: EventRequest):
    world_text.content = f'World {randint(0, 100)}'

# page
page = d.Page(title='Hello world 0', class_='p-10')
page.add(vflex := d.VFlex())

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
g.route('/', page)
app = g.get_app()

if __name__ == '__main__':
    g.run_app(host='0.0.0.0', port=5000)
