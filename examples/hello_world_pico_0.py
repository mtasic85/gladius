from random import randint

from gladius import Gladius, Component, Event
from gladius.html5 import Html5
from gladius.pico import Pico

g = Gladius()
# h = Html5(g)
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

# grid
main.add(grid := p.Grid())
grid.add(d := p.Div('1'))
grid.add(d := p.Div('2'))
grid.add(d := p.Div('3'))
grid.add(d := p.Div('4'))

# header
main.add(h1 := p.H1('Heading 1'))
main.add(h2 := p.H2('Heading 2'))
main.add(h3 := p.H3('Heading 3'))
main.add(h4 := p.H4('Heading 4'))
main.add(h5 := p.H5('Heading 5'))
main.add(h6 := p.H6('Heading 6'))

# hgroup
main.add(hgroup := p.HGroup())
hgroup.add(h2 := p.H2('Heading 2'))
hgroup.add(h3 := p.H3('Subtitle for heading 2'))

# headings
main.add(headings := p.Headings())
headings.add(h2 := p.H2('Heading 2'))
headings.add(h3 := p.H3('Subtitle for heading 2'))

# inline text elements
main.add(div := p.Div())
div.add(abbr := p.Abbr('Abbr.'))
div.add(strong := p.Strong('Bold'))
div.add(b := p.B('Bold'))
div.add(i := p.I('Italic'))
div.add(em := p.Em('Italic'))
div.add(cite := p.Cite('Italic'))
div.add(del_ := p.Del('Deleted'))
div.add(ins := p.Ins('Inserted'))
div.add(kbd := p.Kbd('Ctrl + S'))

main.add(div := p.Div())
div.add(mark := p.Mark('Highlighted'))
div.add(s := p.S('Strikethrough'))
div.add(small := p.Small('Small'))
div.add(p_ := p.P('Text').add(p.Sub('Sub')))
div.add(p_ := p.P('Text').add(p.Sup('Sup')))
div.add(u := p.U('Underline'))

# blockquote
main.add(bq := p.BlockQuote('''
    Maecenas vehicula metus tellus,
    vitae congue turpis hendrerit non.
    Nam at dui sit amet ipsum cursus ornare.
'''))
bq.add(f := p.Footer())
f.add(cite := p.Cite('- Phasellus eget lacinia'))

# links
main.add(div := p.Div())
div.add(a := p.Link('Primary', href='#'))
div.add(a := p.SecondaryLink('Secondary', href='#'))
div.add(a := p.ContrastLink('Contrast', href='#'))

# buttons
main.add(div := p.Div())
div.add(b := p.Button('Button'))
div.add(b := p.SubmitInput())
div.add(b := p.ButtonLink('Link', href='#'))
div.add(b := p.ButtonLink('Link', href='#'))
div.add(b := p.SecondaryButtonLink('Link', href='#'))
div.add(b := p.ContrastButtonLink('Link', href='#'))
div.add(b := p.OutlineButtonLink('Link', href='#'))
div.add(b := p.SecondaryOutlineButtonLink('Link', href='#'))
div.add(b := p.ContrastOutlineButtonLink('Link', href='#'))

# router
g.route('/', page)
app = g.get_app()

if __name__ == '__main__':
    g.run_app(host='0.0.0.0', port=5000)
