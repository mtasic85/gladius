from random import randint

from gladius import Gladius, Component, EventRequest
from gladius.daisyui import DaisyUI

g = Gladius()
ui = DaisyUI(g)

page = ui.Page(title='Hello world', class_='p-10')
page.add(vflex := ui.VFlex())

vflex.add(hello_card := ui.Card())
hello_card.add(hello_text := ui.Text('Hello'))

vflex.add(world_card := ui.Card())
world_card.add(world_text := ui.Text('World'))

async def hello_button_click(button: Component, req: EventRequest):
    hello_text.content = f'Hello {randint(0, 100)}'

async def world_button_click(button: Component, req: EventRequest):
    world_text.content = f'World {randint(0, 100)}'

vflex.add(hflex := ui.Flex())
hflex.add(join := ui.Join())
join.add(btn := ui.Button(class_='btn btn-primary', onclick=hello_button_click).add('Hello'))
join.add(btn := ui.Button(class_='btn btn-secondary', onclick=world_button_click).add('World'))

g.route('/', page)
app = g.get_app()

if __name__ == '__main__':
    g.run_app(host='0.0.0.0', port=5000)
