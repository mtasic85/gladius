from random import randint

from gladius import Gladius, Component, Event
from gladius.daisyui import DaisyUI

g = Gladius()
d = DaisyUI(g)

page = d.Page(title='daisyui layout artboard')
page.add(flex := d.VFlex(class_='p-10 space-y-10'))

flex.add(artboard := d.Artboard())
artboard.add_class('phone-1 artboard-demo bg-[hsl(var(--b3)/var(--tw-bg-opacity))]')
artboard.add(text := d.Text('320×568'))

flex.add(artboard := d.Artboard())
artboard.attrs['class'] += ' phone-2 artboard-demo bg-[hsl(var(--b3)/var(--tw-bg-opacity))]'
artboard.add(text := d.Text('375×667'))

g.route('/', page)
app = g.get_app()

if __name__ == '__main__':
    g.run_app(host='0.0.0.0', port=5000)