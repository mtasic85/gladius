from random import randint

from gladius import Gladius, Component, Event
from gladius.daisyui import DaisyUI

g = Gladius()
d = DaisyUI(g)

# callbacks
async def hello_button_click(button: Component, event: Event):
    hello_text.content = f'Hello {randint(0, 100)}'

async def world_button_click(button: Component, event: Event):
    world_text.content = f'World {randint(0, 100)}'

# page
page = d.Page(title='Hello world 0').add_class('p-10')
page.add(vflex := d.VFlex())

# top cards
vflex.add(card := d.Card())
card.add(hello_text := d.Text('Hello'))

vflex.add(card := d.Card())
card.add(world_text := d.Text('World'))

# buttons
vflex.add(hflex := d.Flex())
hflex.add(join := d.Join())
join.add(button := d.Button('Hello', onclick=hello_button_click).add_class('btn-primary'))
join.add(button := d.Button('World', onclick=world_button_click).add_class('btn-secondary'))

# router
g.route('/', page)
app = g.get_app()

if __name__ == '__main__':
    g.run_app(host='0.0.0.0', port=5000)
