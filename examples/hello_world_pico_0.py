from random import randint

from gladius import Gladius, Component, Event
from gladius.html5 import Html5
from gladius.pico import Pico

g = Gladius()
p = Pico(g)

# callbacks
async def hello_button_click(button: Component, event: Event):
    v: int = randint(0, 100)
    hello_card.data = f'Hello {v}'
    hello_button.data = f'Hello {v}'

async def world_button_click(button: Component, event: Event):
    v: int = randint(0, 100)
    world_card.data = f'World {v}'
    world_button.data = f'World {v}'

# Page
page = p.Page(title='Hello world 0')
page.body.add(main := p.Main())

# Grid
main.add(grid := p.Grid())
grid.add(d := p.Div('1'))
grid.add(d := p.Div('2'))
grid.add(d := p.Div('3'))
grid.add(d := p.Div('4'))

# Header
main.add(h1 := p.H1('Heading 1'))
main.add(h2 := p.H2('Heading 2'))
main.add(h3 := p.H3('Heading 3'))
main.add(h4 := p.H4('Heading 4'))
main.add(h5 := p.H5('Heading 5'))
main.add(h6 := p.H6('Heading 6'))

# HGroup
main.add(hgroup := p.HGroup())
hgroup.add(h2 := p.H2('Heading 2'))
hgroup.add(h3 := p.H3('Subtitle for heading 2'))

# Headings
main.add(headings := p.Headings())
headings.add(h2 := p.H2('Heading 2'))
headings.add(h3 := p.H3('Subtitle for heading 2'))

# Inline text elements
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

# BlockQuote
main.add(bq := p.BlockQuote('''
    Maecenas vehicula metus tellus,
    vitae congue turpis hendrerit non.
    Nam at dui sit amet ipsum cursus ornare.
'''))
bq.add(f := p.Footer())
f.add(cite := p.Cite('- Phasellus eget lacinia'))

# Links
main.add(div := p.Div())
div.add(a := p.Link('Primary', href='#'))
div.add(a := p.SecondaryLink('Secondary', href='#'))
div.add(a := p.ContrastLink('Contrast', href='#'))

# Buttons
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

# Forms
main.add(div := p.Div())
div.add(form := p.Form())
form.add(grid := p.Grid())

grid.add(label := p.Label('First name', for_='firstname'))
label.add(label := p.Input(type='text', id='firstname', name='firstname', placeholder='First name', required='required'))

grid.add(label := p.Label('Last name', for_='lastname'))
label.add(label := p.Input(type='text', id='lastname', name='lastname', placeholder='Last name', required='required'))

form.add(label := p.Label('Email address', for_='email'))
form.add(input_ := p.Input(type='email', id='email', name='email', placeholder='Email address', required='required'))
form.add(small := p.Small("We'll never share your email with anyone else."))

form.add(button := p.Button('Submit', type='submit'))

# Inputs
main.add(div := p.Div())
form.add(input_ := p.Input(type='text', placeholder='Valid', aria_invalid='false'))
form.add(input_ := p.Input(type='text', placeholder='Invalid', aria_invalid='true'))
form.add(input_ := p.Input(type='text', placeholder='Disabled', disabled='disabled'))
form.add(input_ := p.Input(type='text', placeholder='Readonly', disabled='disabled'))

# Select
main.add(div := p.Div())
div.add(label := p.Label('Fruit', for_='fruit'))
div.add(select := p.Select(id='fruit', required='required'))
select.add(option := p.Option('Select a fruit', value='...', selected='selected'))
select.add(option := p.Option('Watermelon', value='watermelon'))
select.add(option := p.Option('Apple', value='apple'))
select.add(option := p.Option('Orange', value='orange'))
select.add(option := p.Option('Mango', value='mango'))

# Radios
main.add(div := p.Div())
div.add(fieldset := p.Fieldset())
fieldset.add(legend := p.Legend('Radios'))

fieldset.add(label := p.Label(for_='small'))
label.add(input_ := p.Input(type='radio', id='small', name='size', value='small', checked='checked'))
label.add(text := p.Text('Small'))

fieldset.add(label := p.Label(for_='medium'))
label.add(input_ := p.Input(type='radio', id='medium', name='size', value='medium'))
label.add(text := p.Text('Medium'))

fieldset.add(label := p.Label(for_='large'))
label.add(input_ := p.Input(type='radio', id='large', name='size', value='small'))
label.add(text := p.Text('Large'))

fieldset.add(label := p.Label(for_='extralarge'))
label.add(input_ := p.Input(type='radio', id='extralarge', name='size', value='small', disabled='disabled'))
label.add(text := p.Text('Extra Large'))

# Checkboxes
fieldset.add(legend := p.Legend('Checkboxes'))

fieldset.add(label := p.Label(for_='terms'))
label.add(input_ := p.Input(type='checkbox', id='terms', name='terms'))
label.add(text := p.Text('I agree to the Terms and Conditions'))

fieldset.add(label := p.Label(for_='terms_sharing'))
label.add(input_ := p.Input(type='checkbox', id='terms_sharing', name='terms_sharing', disabled='disabled', checked='checked'))
label.add(text := p.Text('I agree to share my information with partners'))

fieldset.add(label := p.Label(for_='terms_2'))
label.add(input_ := p.Input(type='checkbox', id='terms_2', name='terms_2', indeterminate='true'))
label.add(text := p.Text('Select all'))

# Switches
fieldset.add(legend := p.Legend('Switches'))

fieldset.add(label := p.Label(for_='switch'))
label.add(input_ := p.Input(type='checkbox', id='switch', name='switch', role='switch'))
label.add(text := p.Text('Publish on my profile'))

fieldset.add(label := p.Label(for_='switch_disabled'))
label.add(input_ := p.Input(type='checkbox', id='switch_disabled', name='switch_disabled', role='switch', disabled='disabled', checked='checked'))
label.add(text := p.Text('User must change password at next logon'))

# Search
fieldset.add(legend := p.Legend(''))
fieldset.add(input_ := p.Input(type='search', id='search', name='search', placeholder='Search'))

# File browser
fieldset.add(label := p.Label('File browser', for_='file'))
label.add(input_ := p.Input(type='file', id='file', name='file'))

# Range slider
fieldset.add(label := p.Label('Range slider', for_='range'))
label.add(input_ := p.Input(type='range', min='0', max='100', value='50', id='range', name='range'))

# Date
fieldset.add(label := p.Label('Date', for_='date'))
label.add(input_ := p.Input(type='date', id='date', name='date'))

# Time
fieldset.add(label := p.Label('Time', for_='time'))
label.add(input_ := p.Input(type='time', id='time', name='time'))

# Color
fieldset.add(label := p.Label('Color', for_='color'))
label.add(input_ := p.Input(type='color', id='color', name='color', value='#0eaaaa'))

# Tables
main.add(figure := p.Figure())

header = ['A', 'B', 'C']
rows = [[j for j in range(i, i + 3)] for i in range(5)]
footer = ['#A', '#B', '#C']
figure.add(table := p.Table(header=header, rows=rows, footer=footer, role='grid'))

# Accordions
main.add(details := p.Details())
details.add(summary := p.Summary('Accordion 1'))
details.add(p_ := p.P('''
    Lorem ipsum dolor sit amet,
    consectetur adipiscing elit.
    Pellentesque urna diam,
    tincidunt nec porta sed,
    auctor id velit.
    Etiam venenatis nisl ut orci consequat,
    vitae tempus quam commodo.
    Nulla non mauris ipsum.
    Aliquam eu posuere orci.
    Nulla convallis lectus rutrum quam hendrerit,
    in facilisis elit sollicitudin.
    Mauris pulvinar pulvinar mi,
    dictum tristique elit auctor quis.
    Maecenas ac ipsum ultrices, porta turpis sit amet, congue turpis.
'''))

main.add(details := p.Details(open='open'))
details.add(summary := p.Summary('Accordion 2'))
details.add(ul := p.Ul())
ul.add(li := p.Li('Vestibulum id elit quis massa interdum sodales.'))
ul.add(li := p.Li('Nunc quis eros vel odio pretium tincidunt nec quis neque.'))
ul.add(li := p.Li('Quisque sed eros non eros ornare elementum.'))
ul.add(li := p.Li('Cras sed libero aliquet, porta dolor quis, dapibus ipsum.'))

# Primary
main.add(details := p.Details())
details.add(summary := p.Summary('Accordion 1', role='button'))

details.add(p_ := p.P('''
    Aenean vestibulum nunc at libero congue,
    eu pretium nulla viverra.
    Fusce sed ex at est egestas vehicula.
    Integer sit amet lectus mi.
    Duis ut viverra mauris, at laoreet enim.
'''))

# Secondary
main.add(details := p.Details())
details.add(summary := p.Summary('Accordion 2', role='button', class_='secondary'))

details.add(p_ := p.P('''
    Quisque porta dictum ipsum nec vestibulum.
    Suspendisse non mi ac tellus scelerisque egestas.
    Sed vel nisi laoreet, rhoncus urna quis, luctus risus.
    Donec vitae molestie felis.
'''))

# Contrast
main.add(details := p.Details())
details.add(summary := p.Summary('Accordion 3', role='button', class_='contrast'))

details.add(p_ := p.P('''
    Praesent quam ipsum, condimentum non augue at,
    porttitor interdum tellus.
    Curabitur ultrices consectetur leo,
    a placerat mauris malesuada et.
    In quis varius risus.
'''))

# Article
main.add(article := p.Article("I'm a card!"))

main.add(article := p.Article())
article.add(header := p.Header('Header'))
article.add(body := p.Text('Body'))
article.add(footer := p.Footer('Footer'))

# router
g.route('/', page)
app = g.get_app()

if __name__ == '__main__':
    g.run_app(host='0.0.0.0', port=5000)
