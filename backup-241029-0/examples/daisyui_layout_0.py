from random import randint

from gladius import Gladius, Component, Event
from gladius.html5 import Html5
from gladius.daisyui import DaisyUI

g = Gladius()
h = Html5(g)
d = DaisyUI(g)

#
# page
#
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

#
# divider
#
main_flex.add(h.H2('Divider'))

# vertical divider
main_flex.add(flex := d.VFlex())
flex.add(div := h.Div('content', class_='grid h-20 card bg-base-300 rounded-box place-items-center'))
flex.add(divider := d.Divider().add(d.Text('OR')))
flex.add(div := h.Div('content', class_='grid h-20 card bg-base-300 rounded-box place-items-center'))

# horizontal divider
main_flex.add(flex := d.Flex())
flex.add(div := h.Div('content', class_='grid h-20 flex-grow card bg-base-300 rounded-box place-items-center'))
flex.add(divider := d.Divider().add_class('divider-horizontal'))
flex.add(div := h.Div('content', class_='grid h-20 flex-grow card bg-base-300 rounded-box place-items-center'))

# lg horizontal divider
main_flex.add(flex := d.Flex().add_class('flex-col lg:flex-row'))
flex.add(div := h.Div('content', class_='grid flex-grow h-32 card bg-base-300 rounded-box place-items-center'))
flex.add(divider := d.Divider().add_class('lg:divider-horizontal').add(d.Text('OR')))
flex.add(div := h.Div('content', class_='grid flex-grow h-32 card bg-base-300 rounded-box place-items-center'))

#
# footer
#
main_flex.add(h.H2('Footer'))

# vertical divider
main_flex.add(footer := d.Footer().add_class('p-10 bg-neutral text-neutral-content'))

footer.add(nav := h.Nav())
nav.add(footer_title := d.FooterTitle('Services'))
nav.add(link := d.Link('Branding').add_class('link-hover'))
nav.add(link := d.Link('Design').add_class('link-hover'))
nav.add(link := d.Link('Marketing').add_class('link-hover'))
nav.add(link := d.Link('Advertisement').add_class('link-hover'))

footer.add(nav := h.Nav())
nav.add(footer_title := d.FooterTitle('Company'))
nav.add(link := d.Link('About us').add_class('link-hover'))
nav.add(link := d.Link('Contact').add_class('link-hover'))
nav.add(link := d.Link('Jobs').add_class('link-hover'))
nav.add(link := d.Link('Press kit').add_class('link-hover'))

footer.add(nav := h.Nav())
nav.add(footer_title := d.FooterTitle('Legal'))
nav.add(link := d.Link('Terms of use').add_class('link-hover'))
nav.add(link := d.Link('Privacy policy').add_class('link-hover'))
nav.add(link := d.Link('Cookie policy').add_class('link-hover'))

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

#
# indicator
#
main_flex.add(h.H2('Indicator'))
main_flex.add(indicator := d.Indicator())
indicator.add(indicator_item := d.IndicatorItem('99+').add_class('badge badge-secondary'))
indicator.add(button := d.Button('Inbox'))

#
# join
#
main_flex.add(h.H2('Join'))
main_flex.add(join := d.Join())
join.add(button := d.Button('Hello').add_class('btn-primary'))
join.add(button := d.Button('World').add_class('btn-secondary'))

#
# stack
#
main_flex.add(h.H2('Stack'))
main_flex.add(stack := d.Stack())
stack.add(h.Div('1', class_='grid w-32 h-20 rounded bg-primary text-primary-content place-content-center'))
stack.add(h.Div('2', class_='grid w-32 h-20 rounded bg-accent text-accent-content place-content-center'))
stack.add(h.Div('3', class_='grid w-32 h-20 rounded bg-secondary text-secondary-content place-content-center'))

#
# toast
#
main_flex.add(h.H2('Toast'))
main_flex.add(toast := d.Toast().add_class('toast-top toast-end'))
toast.add(alert := d.Alert().add_class('alert-info'))
alert.add(span := h.Span('New mail arrived.'))
toast.add(alert := d.Alert().add_class('alert-success'))
alert.add(span := h.Span('Message sent successfully.'))

g.route('/', page)
app = g.get_app()

if __name__ == '__main__':
    g.run_app(host='0.0.0.0', port=5000)
