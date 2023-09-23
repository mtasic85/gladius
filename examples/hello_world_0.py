from random import randint

from gladius import Gladius, Component, EventRequest
from gladius.daisyui import DaisyUI

# glados daisyui
g = Gladius()
dui = DaisyUI(g)

# callbacks
async def hello_button_click(button: Component, req: EventRequest):
    hello_text.content = f'Hello {randint(0, 100)}'

async def world_button_click(button: Component, req: EventRequest):
    world_text.content = f'World {randint(0, 100)}'

# page
page = dui.Page(title='Hello world 0', class_='p-10')
page.add(vflex := dui.VFlex())

# top cards
vflex.add(card := dui.Card())
card.add(hello_text := dui.Text('Hello'))

vflex.add(card := dui.Card())
card.add(world_text := dui.Text('World'))

# buttons
vflex.add(hflex := dui.Flex())
hflex.add(join := dui.Join())
join.add(button := dui.Button(class_='btn btn-primary', onclick=hello_button_click))
button.add(text := dui.Text('Hello'))
join.add(button := dui.Button(class_='btn btn-success', onclick=world_button_click))
button.add(text := dui.Text('World'))

# router
g.route('/', page)
app = g.get_app()

if __name__ == '__main__':
    g.run_app(host='0.0.0.0', port=5000)
