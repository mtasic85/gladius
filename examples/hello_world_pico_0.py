from random import randint

from gladius import Gladius, Component, Event
from gladius.html5 import Html5
from gladius.pico import Pico

g = Gladius()
h = Html5(g)
p = Pico(g)

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
page = p.Page(title='Hello world 0')
page.body.add(main := p.Main())

main.add(grid := p.Grid())
grid.add(d := h.Div('1'))
grid.add(d := h.Div('2'))
grid.add(d := h.Div('3'))
grid.add(d := h.Div('4'))

main.add(h1 := h.H1('Heading 1'))
main.add(h2 := h.H2('Heading 2'))
main.add(h3 := h.H3('Heading 3'))
main.add(h4 := h.H4('Heading 4'))
main.add(h5 := h.H5('Heading 5'))
main.add(h6 := h.H6('Heading 6'))

# router
g.route('/', page)
app = g.get_app()

if __name__ == '__main__':
    g.run_app(host='0.0.0.0', port=5000)
