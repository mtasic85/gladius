from random import randint

from gladius import Gladius, Component, EventRequest
from gladius.daisyui import DaisyUI

# glados daisyui
g = Gladius()
ui = DaisyUI(g)

# callbacks
async def hello_button_click(button: Component, req: EventRequest):
    hello_text.content = f'Hello {randint(0, 100)}'

async def world_button_click(button: Component, req: EventRequest):
    world_text.content = f'World {randint(0, 100)}'

# page
page = ui.Page(title='Hello world 0', class_='p-10')
page.add(vflex := ui.VFlex())

# top cards
vflex.add(card := ui.Card())
card.add(hello_text := ui.Text('Hello'))

vflex.add(card := ui.Card())
card.add(world_text := ui.Text('World'))

# buttons
vflex.add(hflex := ui.Flex())
hflex.add(join := ui.Join())
join.add(button := ui.Button(class_='btn btn-primary', onclick=hello_button_click).add('Hello'))
join.add(join := ui.Button(class_='btn btn-success', onclick=world_button_click).add('World'))

# router
g.route('/', page)
app = g.get_app()

if __name__ == '__main__':
    g.run_app(host='0.0.0.0', port=5000)
