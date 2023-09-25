from random import randint

from gladius import Gladius, Component, Event
from gladius.daisyui import DaisyUI

g = Gladius()
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

# page
page = d.Page(title='Hello world 0').add_class('p-10')
page.add(vflex := d.VFlex())

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
