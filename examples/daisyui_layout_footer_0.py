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
main_flex.add(footer := d.Footer().add_class('p-10 bg-neutral text-neutral-content'))

footer.add(nav := h.Nav())
nav.add(footer_title := d.FooterTitle().add(d.Text('Services')))
nav.add(link := d.Link().add_class('link-hover').add(d.Text('Branding')))
nav.add(link := d.Link().add_class('link-hover').add(d.Text('Design')))
nav.add(link := d.Link().add_class('link-hover').add(d.Text('Marketing')))
nav.add(link := d.Link().add_class('link-hover').add(d.Text('Advertisement')))

footer.add(nav := h.Nav())
nav.add(footer_title := d.FooterTitle().add(d.Text('Company')))
nav.add(link := d.Link().add_class('link-hover').add(d.Text('About us')))
nav.add(link := d.Link().add_class('link-hover').add(d.Text('Contact')))
nav.add(link := d.Link().add_class('link-hover').add(d.Text('Jobs')))
nav.add(link := d.Link().add_class('link-hover').add(d.Text('Press kit')))

footer.add(nav := h.Nav())
nav.add(footer_title := d.FooterTitle().add(d.Text('Legal')))
nav.add(link := d.Link().add_class('link-hover').add(d.Text('Terms of use')))
nav.add(link := d.Link().add_class('link-hover').add(d.Text('Privacy policy')))
nav.add(link := d.Link().add_class('link-hover').add(d.Text('Cookie policy')))

g.route('/', page)
app = g.get_app()

if __name__ == '__main__':
    g.run_app(host='0.0.0.0', port=5000)
