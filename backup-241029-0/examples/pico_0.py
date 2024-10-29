from random import randint

from gladius import Gladius, Component, Event
from gladius.pico import Pico

g = Gladius()
p = Pico(g)

# Page
page = p.Page(title='Pico.css - 0')

page.head.add(style := p.Style('''
  #grid.grid > * {
    padding: calc(var(--spacing)/ 2) 0;
    border-radius: var(--border-radius);
    background: var(--code-background-color);
    font-size: 87.5%;
    text-align: center;
  }

  dialog.example {
    background-color: inherit;
  }

  dialog.example {
    display: block;
    z-index: inherit;
    position: relative;
    top: inherit;
    right: inherit;
    bottom: inherit;
    left: inherit;
    align-items: inherit;
    justify-content: inherit;
    width: inherit;
    min-width: inherit;
    height: inherit;
    min-height: inherit;
    padding: 0;
    background-color: inherit;
  }
'''))

# main container
page.add(main := p.Main())
main.add(h1 := p.H1('Pico.css'))
main.add(hr := p.Hr())

# Header
main.add(h1 := p.H1('Heading 1'))
main.add(h2 := p.H2('Heading 2'))
main.add(h3 := p.H3('Heading 3'))
main.add(h4 := p.H4('Heading 4'))
main.add(h5 := p.H5('Heading 5'))
main.add(h6 := p.H6('Heading 6'))

main.add(hr := p.Hr())

# Grid
# main container-fluid enable a 100% layout
page.add(main := p.Main(class_='container-fluid'))
main.add(h2 := p.H2(r'Grid - 100% Layout'))

main.add(grid := p.Grid(id='grid'))
grid.add(d := p.Div('1'))
grid.add(d := p.Div('2'))
grid.add(d := p.Div('3'))
grid.add(d := p.Div('4'))

main.add(hr := p.Hr())

# Grid
#
page.add(main := p.Main(class_='container'))
main.add(h2 := p.H2('Grid'))

main.add(grid := p.Grid(id='grid'))
grid.add(d := p.Div('1'))
grid.add(d := p.Div('2'))
grid.add(d := p.Div('3'))
grid.add(d := p.Div('4'))

main.add(hr := p.Hr())

# HGroup
main.add(h2 := p.H2('HGroup'))

main.add(hgroup := p.HGroup())
hgroup.add(h2 := p.H2('Heading 2'))
hgroup.add(h3 := p.H3('Subtitle for heading 2'))

main.add(hr := p.Hr())

# Headings
main.add(h2 := p.H2('Headings'))

main.add(headings := p.Headings())
headings.add(h2 := p.H2('Heading 2'))
headings.add(h3 := p.H3('Subtitle for heading 2'))

main.add(hr := p.Hr())

# Inline text elements
main.add(h2 := p.H2('Inline text elements'))

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

main.add(hr := p.Hr())

# BlockQuote
main.add(h2 := p.H2('BlockQuote'))

main.add(bq := p.BlockQuote('''
    Maecenas vehicula metus tellus,
    vitae congue turpis hendrerit non.
    Nam at dui sit amet ipsum cursus ornare.
'''))
bq.add(f := p.Footer())
f.add(cite := p.Cite('- Phasellus eget lacinia'))

main.add(hr := p.Hr())

# Links
main.add(h2 := p.H2('Links'))

main.add(div := p.Div())
div.add(a := p.A('Primary', href='#'))
div.add(a := p.A('Secondary', href='#', class_='secondary'))
div.add(a := p.A('Contrast', href='#', class_='contrast'))

main.add(hr := p.Hr())

# Buttons
main.add(h2 := p.H2('Buttons'))

main.add(div := p.Div())
div.add(b := p.Button('Button'))
div.add(b := p.Input('Button', type='submit'))
div.add(b := p.A('Link', href='#', role='button'))
div.add(b := p.A('Link', href='#', role='button', class_='secondary'))
div.add(b := p.A('Link', href='#', role='button', class_='contrast'))
div.add(b := p.A('Link', href='#', role='button', class_='outline'))
div.add(b := p.A('Link', href='#', role='button', class_='secondary outline'))
div.add(b := p.A('Link', href='#', role='button', class_='contrast outline'))

main.add(hr := p.Hr())

# Forms
main.add(h2 := p.H2('Forms'))

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

main.add(hr := p.Hr())

# Inputs
main.add(h2 := p.H2('Inputs'))

main.add(div := p.Div())
form.add(input_ := p.Input(type='text', placeholder='Valid', aria_invalid='false'))
form.add(input_ := p.Input(type='text', placeholder='Invalid', aria_invalid='true'))
form.add(input_ := p.Input(type='text', placeholder='Disabled', disabled='disabled'))
form.add(input_ := p.Input(type='text', placeholder='Readonly', disabled='disabled'))

main.add(hr := p.Hr())

# Select
main.add(h2 := p.H2('Select'))

main.add(div := p.Div())
div.add(label := p.Label('Fruit', for_='fruit'))
div.add(select := p.Select(id='fruit', required='required'))
select.add(option := p.Option('Select a fruit', value='...', selected='selected'))
select.add(option := p.Option('Watermelon', value='watermelon'))
select.add(option := p.Option('Apple', value='apple'))
select.add(option := p.Option('Orange', value='orange'))
select.add(option := p.Option('Mango', value='mango'))

main.add(hr := p.Hr())

# Radios
main.add(h2 := p.H2('Radios'))

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

main.add(hr := p.Hr())

# Checkboxes
main.add(h2 := p.H2('Checkboxes'))

main.add(div := p.Div())
div.add(fieldset := p.Fieldset())
fieldset.add(legend := p.Legend('Checkboxes'))

fieldset.add(label := p.Label(for_='terms'))
label.add(input_ := p.Input(type='checkbox', id='terms', name='terms'))
label.add(text := p.Text('I agree to the Terms and Conditions'))

fieldset.add(label := p.Label(for_='terms_sharing'))
label.add(input_ := p.Input(type='checkbox', id='terms_sharing', name='terms_sharing', disabled='disabled', checked='checked'))
label.add(text := p.Text('I agree to share my information with partners'))

fieldset.add(label := p.Label(for_='terms_2'))
label.add(input_ := p.Input(type='checkbox', id='indeterminate-checkbox', name='terms_2', indeterminate='indeterminate'))
label.add(text := p.Text('Select all'))

main.add(hr := p.Hr())

# Switches
main.add(h2 := p.H2('Switches'))

main.add(div := p.Div())
div.add(fieldset := p.Fieldset())
fieldset.add(legend := p.Legend('Switches'))

fieldset.add(label := p.Label(for_='switch'))
label.add(input_ := p.Input(type='checkbox', id='switch', name='switch', role='switch'))
label.add(text := p.Text('Publish on my profile'))

fieldset.add(label := p.Label(for_='switch_disabled'))
label.add(input_ := p.Input(type='checkbox', id='switch_disabled', name='switch_disabled', role='switch', disabled='disabled', checked='checked'))
label.add(text := p.Text('User must change password at next logon'))

main.add(hr := p.Hr())

# Search
main.add(h2 := p.H2('Search'))

main.add(div := p.Div())
div.add(fieldset := p.Fieldset())
fieldset.add(legend := p.Legend(''))
fieldset.add(input_ := p.Input(type='search', id='search', name='search', placeholder='Search'))

main.add(hr := p.Hr())

# File browser
main.add(h2 := p.H2('File browser'))

main.add(div := p.Div())
div.add(fieldset := p.Fieldset())
fieldset.add(label := p.Label('File browser', for_='file'))
label.add(input_ := p.Input(type='file', id='file', name='file'))

main.add(hr := p.Hr())

# Range slider
main.add(h2 := p.H2('Range slider'))

main.add(div := p.Div())
div.add(fieldset := p.Fieldset())
fieldset.add(label := p.Label('Range slider', for_='range'))
label.add(input_ := p.Input(type='range', min='0', max='100', value='50', id='range', name='range'))

main.add(hr := p.Hr())

# Date
main.add(h2 := p.H2('Date'))

main.add(div := p.Div())
div.add(fieldset := p.Fieldset())
fieldset.add(label := p.Label('Date', for_='date'))
label.add(input_ := p.Input(type='date', id='date', name='date'))

main.add(hr := p.Hr())

# Time
main.add(h2 := p.H2('Time'))

main.add(div := p.Div())
div.add(fieldset := p.Fieldset())
fieldset.add(label := p.Label('Time', for_='time'))
label.add(input_ := p.Input(type='time', id='time', name='time'))

main.add(hr := p.Hr())

# Color
main.add(h2 := p.H2('Color'))

main.add(div := p.Div())
div.add(fieldset := p.Fieldset())
fieldset.add(label := p.Label('Color', for_='color'))
label.add(input_ := p.Input(type='color', id='color', name='color', value='#0eaaaa'))

main.add(hr := p.Hr())

# Tables
main.add(h2 := p.H2('Tables'))

main.add(figure := p.Figure())
header = ['A', 'B', 'C']
rows = [[j for j in range(i, i + 3)] for i in range(5)]
footer = ['#A', '#B', '#C']
figure.add(table := p.Table(header=header, rows=rows, footer=footer, role='grid'))

main.add(hr := p.Hr())

# Accordions
main.add(h2 := p.H2('Accordions'))

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

main.add(hr := p.Hr())

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

main.add(hr := p.Hr())

# Article
main.add(h2 := p.H2('Article'))

main.add(article := p.Article("I'm a card!"))

main.add(article := p.Article())
article.add(header := p.Header('Header'))
article.add(body := p.Text('Body'))
article.add(footer := p.Footer('Footer'))

main.add(hr := p.Hr())

# Dropdown
main.add(h2 := p.H2('Dropdown'))

main.add(details := p.Details(role='list'))
details.add(summary := p.Summary('Dropdown', aria_haspopup='listbox'))
details.add(ul := p.Ul(role='listbox'))
ul.add(li := p.Li().add(a := p.A('Action')))
ul.add(li := p.Li().add(a := p.A('Another action')))
ul.add(li := p.Li().add(a := p.A('Something else here')))

# Select
main.add(select := p.Select())
select.add(option := p.Option('Select', value='', disabled='disabled', selected='selected'))
select.add(option := p.Option('Option', value=''))
select.add(option := p.Option('Another option', value=''))
select.add(option := p.Option('Something else here', value=''))

# Primary
main.add(details := p.Details(role='list'))
details.add(summary := p.Summary('Dropdown as a button 1', aria_haspopup='listbox', role='button'))
details.add(ul := p.Ul(role='listbox'))
ul.add(li := p.Li().add(a := p.A('Action')))
ul.add(li := p.Li().add(a := p.A('Another action')))
ul.add(li := p.Li().add(a := p.A('Something else here')))

# Secondary
main.add(details := p.Details(role='list'))
details.add(summary := p.Summary('Dropdown as a button 2', aria_haspopup='listbox', role='button', class_='secondary'))
details.add(ul := p.Ul(role='listbox'))
ul.add(li := p.Li().add(a := p.A('Action')))
ul.add(li := p.Li().add(a := p.A('Another action')))
ul.add(li := p.Li().add(a := p.A('Something else here')))

# Contrast
main.add(details := p.Details(role='list'))
details.add(summary := p.Summary('Dropdown as a button 3', aria_haspopup='listbox', role='button', class_='contrast'))
details.add(ul := p.Ul(role='listbox'))
ul.add(li := p.Li().add(a := p.A('Action')))
ul.add(li := p.Li().add(a := p.A('Another action')))
ul.add(li := p.Li().add(a := p.A('Something else here')))

# With radio buttons
main.add(details := p.Details(role='list'))
details.add(summary := p.Summary('Dropdown', aria_haspopup='listbox'))
details.add(ul := p.Ul(role='listbox'))
ul.add(li := p.Li())

li.add(label := p.Label(for_='small'))
label.add(input_ := p.Input(type='radio', id='small', name='size', value='small', checked='checked'))
label.add(text := p.Text('Small'))

li.add(label := p.Label(for_='medium'))
label.add(input_ := p.Input(type='radio', id='medium', name='size', value='medium'))
label.add(text := p.Text('Medium'))

li.add(label := p.Label(for_='large'))
label.add(input_ := p.Input(type='radio', id='large', name='size', value='large'))
label.add(text := p.Text('Large'))

# With checkboxes
main.add(details := p.Details(role='list'))
details.add(summary := p.Summary('Dropdown', aria_haspopup='listbox'))
details.add(ul := p.Ul(role='listbox'))
ul.add(li := p.Li())

li.add(label := p.Label())
label.add(input_ := p.Input(type='checkbox'))
label.add(text := p.Text('Small'))

li.add(label := p.Label())
label.add(input_ := p.Input(type='checkbox'))
label.add(text := p.Text('Medium'))

li.add(label := p.Label())
label.add(input_ := p.Input(type='checkbox'))
label.add(text := p.Text('Large'))

# Nav with dropdown
main.add(nav := p.Nav())
nav.add(ul := p.Ul())
ul.add(li := p.Li())
li.add(strong := p.Strong('Brand'))

nav.add(ul := p.Ul())
ul.add(li := p.Li())
li.add(a := p.A('Link', href='#'))
ul.add(li := p.Li())
li.add(details := p.Details(role='list', dir='rtl'))
details.add(summary := p.Summary('Dropdown', aria_haspopup='listbox', role='link'))
details.add(ul := p.Ul(role='listbox'))
ul.add(li := p.Li().add(a := p.A('Action')))
ul.add(li := p.Li().add(a := p.A('Another action')))
ul.add(li := p.Li().add(a := p.A('Something else here')))

main.add(hr := p.Hr())

# Nav with dropdowns
main.add(nav := p.Nav())

nav.add(ul := p.Ul())
ul.add(li := p.Li())
li.add(details := p.Details(role='list'))
details.add(summary := p.Summary('Dropdown', aria_haspopup='listbox'))
details.add(ul := p.Ul(role='listbox'))
ul.add(li := p.Li().add(a := p.A('Action')))
ul.add(li := p.Li().add(a := p.A('Another action')))
ul.add(li := p.Li().add(a := p.A('Something else here')))

nav.add(ul := p.Ul())
ul.add(li := p.Li())
li.add(details := p.Details(role='list'))
details.add(summary := p.Summary('Dropdown', aria_haspopup='listbox', role='button'))
details.add(ul := p.Ul(role='listbox'))
ul.add(li := p.Li().add(a := p.A('Action')))
ul.add(li := p.Li().add(a := p.A('Another action')))
ul.add(li := p.Li().add(a := p.A('Something else here')))

main.add(hr := p.Hr())

# Nav with dropdown hover
main.add(nav := p.Nav())
nav.add(ul := p.Ul())
ul.add(li := p.Li())
li.add(strong := p.Strong('Brand'))

nav.add(ul := p.Ul())

ul.add(li := p.Li())
li.add(a := p.A('Link', href='#'))

ul.add(li := p.Li())
li.add(a := p.A('Link', href='#'))

ul.add(li := p.Li(role='list', dir='rtl'))
li.add(a := p.A('Dropdown', href='#', aria_haspopup='listbox'))
li.add(ul2 := p.Ul(role='listbox'))
ul2.add(li := p.Li().add(a := p.A('Action')))
ul2.add(li := p.Li().add(a := p.A('Another action')))
ul2.add(li := p.Li().add(a := p.A('Something else here')))

main.add(hr := p.Hr())

# Modal
main.add(h2 := p.H2('Modal'))

main.add(dialog := p.Dialog(open='open', class_='example'))
dialog.add(article := p.Article())
article.add(header := p.Header())
header.add(a := p.A(href='#close', aria_label='Close', class_='close'))
header.add(text := p.Text('Modal title'))
article.add(p_ := p.P('''
    Nunc nec ligula a tortor sollicitudin dictum in vel enim. 
    Quisque facilisis turpis vel eros dictum aliquam et nec turpis. 
    Sed eleifend a dui nec ullamcorper. 
    Praesent vehicula lacus ac justo accumsan ullamcorper.
'''))

main.add(hr := p.Hr())

# Modal with footer
main.add(dialog := p.Dialog(open='open', class_='example'))
dialog.add(article := p.Article())
article.add(header := p.Header())
header.add(a := p.A(href='#close', aria_label='Close', class_='close'))
header.add(text := p.Text('Modal title'))
article.add(p_ := p.P('''
    Nunc nec ligula a tortor sollicitudin dictum in vel enim. 
    Quisque facilisis turpis vel eros dictum aliquam et nec turpis. 
    Sed eleifend a dui nec ullamcorper. 
    Praesent vehicula lacus ac justo accumsan ullamcorper.
'''))
article.add(footer := p.Footer())
footer.add(a := p.A('Cancel', href='#cancel', role='button', class_='secondary'))
footer.add(a := p.A('Confirm', href='#confirm', role='button'))

main.add(hr := p.Hr())

# Button to trigger the modal
main.add(div := p.Div())
div.add(button := p.Button('Launch demo modal', class_='contrast', data_target='modal-example', onClick='toggleModal(event)'))

main.add(dialog := p.Dialog(id='modal-example'))
dialog.add(article := p.Article())
article.add(a := p.A(href='#close', aria_label='Close', class_='close', data_target='modal-example', onClick='toggleModal(event)'))
article.add(h3 := p.H3('Confirm your action!'))
article.add(p_ := p.P('''
    Cras sit amet maximus risus. 
    Pellentesque sodales odio sit amet augue finibus pellentesque. 
    Nullam finibus risus non semper euismod.
'''))
article.add(footer := p.Footer())
footer.add(a := p.A('Cancel', href='#cancel', role='button', class_='secondary', data_target='modal-example', onClick='toggleModal(event)'))
footer.add(a := p.A('Confirm', href='#confirm', role='button', data_target='modal-example', onClick='toggleModal(event)'))

main.add(hr := p.Hr())

# Navs
main.add(h2 := p.H2('Navs'))

main.add(nav := p.Nav())
nav.add(ul := p.Ul())
ul.add(li := p.Li())
li.add(strong := p.Strong('Brand'))

nav.add(ul := p.Ul())
ul.add(li := p.Li())
li.add(a := p.A('Link', href='#', onclick='event.preventDefault()', class_='secondary', aria_label='Menu'))

ul.add(li := p.Li())
li.add(a := p.A('Link', href='#'))

ul.add(li := p.Li())
li.add(a := p.A('Button', href='#', role='button'))

main.add(hr := p.Hr())

# Navs with icons
main.add(nav := p.Nav())

nav.add(ul := p.Ul())
ul.add(li := p.Li())
li.add(a := p.A('''
  <svg aria-hidden="true" focusable="false" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" height="16px" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="--darkreader-inline-stroke: currentColor;" data-darkreader-inline-stroke=""><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
''', href='#', class_='secondary'))

nav.add(ul := p.Ul())
ul.add(li := p.Li())
li.add(strong := p.Strong('Brand'))

nav.add(ul := p.Ul())
ul.add(li := p.Li())
li.add(a := p.A('''
  <svg aria-hidden="true" focusable="false" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" height="16px" fill="currentColor" stroke="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="--darkreader-inline-stroke: none; --darkreader-inline-fill: currentColor;" data-darkreader-inline-stroke="" data-darkreader-inline-fill=""><path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path></svg>
''', href='#', class_='secondary'))

main.add(hr := p.Hr())

# Navs stacked vertically
main.add(aside := p.Aside())
aside.add(nav := p.Nav())

nav.add(ul := p.Ul())
ul.add(li := p.Li())
li.add(a := p.A('Link', href='#'))
li.add(a := p.A('Link', href='#'))
li.add(a := p.A('Link', href='#'))

main.add(hr := p.Hr())

# Nav breadcrumb
main.add(nav := p.Nav(aria_label='breadcrumb'))
nav.add(ul := p.Ul())
ul.add(li := p.Li())
li.add(a := p.A('Home', href='#'))
ul.add(li := p.Li())
li.add(a := p.A('Category', href='#'))
ul.add(li := p.Li())
li.add(text := p.Text('Page'))

main.add(hr := p.Hr())

# Progress
main.add(h2 := p.H2('Progress'))

main.add(progress := p.Progress(value='25', max='100'))
main.add(progress := p.Progress())

main.add(hr := p.Hr())

# Loading
main.add(h2 := p.H2('Loading'))

main.add(button := p.Button('Please wait...', aria_busy='true'))
main.add(button := p.Button(aria_busy='true', class_='secondary'))
main.add(article := p.Article(aria_busy='true'))
main.add(a := p.A('Generating link, please wait', href='#', aria_busy='true'))

main.add(hr := p.Hr())

# Tooltips
main.add(h2 := p.H2('Tooltips'))

main.add(p_ := p.P())
p_.add(text := p.Text('Tooltip on a'))
p_.add(a := p.A('link', href='#', data_tooltip='Tooltip'))

main.add(p_ := p.P())
p_.add(text := p.Text('Tooltip on'))
p_.add(em := p.Em('inline element', data_tooltip='Tooltip'))

main.add(p_ := p.P())
p_.add(button := p.Button('Tooltip on a button', data_tooltip='Tooltip'))

main.add(hr := p.Hr())

# Tooltips placement
main.add(grid := p.Grid())
grid.add(div := p.Div())
div.add(button := p.Button('Top', data_tooltip='Top', data_placement='top'))
grid.add(div := p.Div())
div.add(button := p.Button('Right', data_tooltip='Right', data_placement='right'))
grid.add(div := p.Div())
div.add(button := p.Button('Bottom', data_tooltip='Bottom', data_placement='bottom'))
grid.add(div := p.Div())
div.add(button := p.Button('Left', data_tooltip='Left', data_placement='left'))

main.add(hr := p.Hr())

# router
g.route('/', page)
app = g.get_app()

if __name__ == '__main__':
    g.run_app(host='0.0.0.0', port=5000)
