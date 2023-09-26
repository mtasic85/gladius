from random import randint

from gladius import Gladius, Component, Event
from gladius.daisyui import DaisyUI

g = Gladius()
d = DaisyUI(g)

def my_navbar() -> Component:
    # navbar = d.Navbar(hx_boost='true')
    navbar = d.Navbar()
    navbar.add(a := d.NavbarButton('Home', href='/'))
    navbar.add(a := d.NavbarButton('Dashboard', href='/dashboard'))
    navbar.add(a := d.NavbarButton('Sign In', href='/signin'))
    navbar.add(a := d.NavbarButton('Sign Up', href='/signup'))
    return navbar

def my_join() -> Component:
    # join = d.Join(hx_boost='true')
    join = d.Join()
    join.add(a := d.Link('Home', class_='btn join-item', href='/'))
    join.add(a := d.Link('Dashboard', class_='btn join-item', href='/dashboard'))
    join.add(a := d.Link('Sign In', class_='btn join-item', href='/signin'))
    join.add(a := d.Link('Sign Up', class_='btn join-item', href='/signup'))
    return join

def root_page() -> Component:
    # root/index
    page = d.Page(title='Multi Page 0')

    # navbar
    page.add(navbar := my_navbar())

    # join buttons
    page.add(flex := d.Flex().add_class('gap-2'))
    flex.add(join := my_join())
    return page

def dashboard_page() -> Component:
    page = d.Page(title='Dashboard')
    page.add(navbar := my_navbar())
    
    # vflex - Hello World
    page.add(vflex := d.VFlex().add_class('gap-2'))
    vflex.add(card := d.Card('Hello'))
    vflex.add(flex := d.Flex().add_class('gap-2'))
    flex.add(card := d.Card('World'))
    flex.add(card := d.Card('!'))
    
    async def add_button_click(button, event: Event):
        row = [randint(0, 10) for i in range(3)]
        table_0.rows = [*table_0.rows, row]
        
        row = [randint(10, 100) for i in range(3)]
        table_1.rows = [*table_1.rows, row]

    async def remove_button_click(button, event: Event):
        table_0.rows = [*table_0.rows[:-1]]
        table_1.rows = [*table_1.rows[:-1]]
    
    # join button
    vflex.add(join := d.Join())
    join.add(add_button := d.Button('Add', onclick=add_button_click))
    join.add(edit_button := d.Button('Edit', class_='btn btn-secondary'))
    join.add(remove_button := d.Button('Remove', onclick=remove_button_click, class_='btn btn-primary'))

    # table_0
    header = ['A', 'B', 'C']
    rows = [[j for j in range(i, i + 3)] for i in range(5)]
    vflex.add(table_0 := d.Table(header=header, rows=rows))
    
    # table_1
    header = ['D', 'E', 'F']
    rows = [[j for j in range(i, i + 3)] for i in range(100, 105)]
    vflex.add(table_1 := d.Table(header=header, rows=rows))
    return page

def sign_in_page() -> Component:
    page = d.Page(title='Sign In')
    page.add(navbar := my_navbar())
    page.add(d.Text('Sign In'))
    return page

def sign_up_page() -> Component:
    page = d.Page(title='Sign Up')
    page.add(navbar := my_navbar())
    page.add(d.Text('Sign Up'))
    return page

g.route('/', root_page())
g.route('/dashboard', dashboard_page())
g.route('/signin', sign_in_page())
g.route('/signup', sign_up_page())
app = g.get_app()

if __name__ == '__main__':
    g.run_app(host='0.0.0.0', port=5000)
