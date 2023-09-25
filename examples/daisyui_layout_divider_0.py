from random import randint

from gladius import Gladius, Component, Event
from gladius.html5 import Html5
from gladius.daisyui import DaisyUI

g = Gladius()
h = Html5(g)
d = DaisyUI(g)

page = d.Page(title='daisyui layout artboard')
page.add(main_flex := d.VFlex(class_='p-10 space-y-10'))

# vertical divider
main_flex.add(flex := d.VFlex())
flex.add(div := h.Div(class_='grid h-20 card bg-base-300 rounded-box place-items-center').add(d.Text('content')))
flex.add(divider := d.Divider().add(d.Text('OR')))
flex.add(div := h.Div(class_='grid h-20 card bg-base-300 rounded-box place-items-center').add(d.Text('content')))

# horizontal divider
main_flex.add(flex := d.Flex())
flex.add(div := h.Div(class_='grid h-20 flex-grow card bg-base-300 rounded-box place-items-center').add(d.Text('content')))
flex.add(divider := d.Divider().add_class('divider-horizontal'))
flex.add(div := h.Div(class_='grid h-20 flex-grow card bg-base-300 rounded-box place-items-center').add(d.Text('content')))

# lg horizontal divider
main_flex.add(flex := d.Flex().add_class('flex-col lg:flex-row'))
flex.add(div := h.Div(class_='grid flex-grow h-32 card bg-base-300 rounded-box place-items-center').add(d.Text('content')))
flex.add(divider := d.Divider().add_class('lg:divider-horizontal').add(d.Text('OR')))
flex.add(div := h.Div(class_='grid flex-grow h-32 card bg-base-300 rounded-box place-items-center').add(d.Text('content')))

g.route('/', page)
app = g.get_app()

if __name__ == '__main__':
    g.run_app(host='0.0.0.0', port=5000)