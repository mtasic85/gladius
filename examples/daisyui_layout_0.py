from random import randint

from gladius import Gladius, Component, Event
from gladius.html5 import Html5
from gladius.daisyui import DaisyUI

g = Gladius()
h = Html5(g)
d = DaisyUI(g)

page = d.Page(title='daisyui layout')
page.add(main_flex := d.VFlex(class_='p-10 space-y-10 prose'))
main_flex.add(h.H1('Layout'))

#
# artboard
#
main_flex.add(h.H2('Artboard'))

main_flex.add(artboard := d.Artboard())
artboard.add_class('phone-1 artboard-demo bg-[hsl(var(--b3)/var(--tw-bg-opacity))]')
artboard.add(text := d.Text('320×568'))

main_flex.add(artboard := d.Artboard())
artboard.attrs['class'] += ' phone-2 artboard-demo bg-[hsl(var(--b3)/var(--tw-bg-opacity))]'
artboard.add(text := d.Text('375×667'))

#
# divider
#
main_flex.add(h.H2('Divider'))

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

#
# footer
#
main_flex.add(h.H2('Footer'))

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

#
# hero
#
main_flex.add(h.H2('Hero'))
main_flex.add(hero := d.Hero())
hero.add(hero_content := d.HeroContent().add_class('text-center'))
hero_content.add(div := h.Div(class_='max-w-md'))
div.add(h.H1('Hello there', class_='text-5xl font-bold'))
div.add(h.P('Provident cupiditate voluptatem et in. Quaerat fugiat ut assumenda excepturi exercitationem quasi. In deleniti eaque aut repudiandae et a id nisi.', class_='py-6'))
div.add(d.Button('Get Started').add_class('btn-primary'))

g.route('/', page)
app = g.get_app()

if __name__ == '__main__':
    g.run_app(host='0.0.0.0', port=5000)
