from random import randint

from gladius import Gladius, Component, EventRequest
from gladius.daisyui import DaisyUI

g = Gladius()
dui = DaisyUI(g)

def my_navbar() -> Component:
    navbar = dui.Navbar(hx_boost='true')
    navbar.add(a := dui.Link(href='/').add(dui.Text('Home')))
    navbar.add(a := dui.Link(href='/dashboard').add(dui.Text('Dashboard')))
    navbar.add(a := dui.Link(href='/signin').add(dui.Text('Sign In')))
    navbar.add(a := dui.Link(href='/signup').add(dui.Text('Sign Up')))
    return navbar

def my_join() -> Component:
    join = dui.Join(hx_boost='true')
    join.add(a := dui.Link(class_='btn join-item', href='/').add(dui.Text('Home')))
    join.add(a := dui.Link(class_='btn join-item', href='/dashboard').add(dui.Text('Dashboard')))
    join.add(a := dui.Link(class_='btn join-item', href='/signin').add(dui.Text('Sign In')))
    join.add(a := dui.Link(class_='btn join-item', href='/signup').add(dui.Text('Sign Up')))
    return join

def root_page() -> Component:
    # root/index
    page = dui.Page(title='Multi Page 0')

    # navbar
    page.add(navbar := my_navbar())

    # join buttons
    page.add(flex := dui.Flex())
    flex.add(join := my_join())
    return page

def dashboard_page() -> Component:
    page = dui.Page(title='Dashboard')
    page.add(navbar := my_navbar())
    
    # vflex - Hello World
    page.add(vflex := dui.VFlex())
    vflex.add(card := dui.Card().add(dui.Text('Hello')))
    vflex.add(flex := dui.Flex())
    flex.add(card := dui.Card().add(dui.Text('World')))
    flex.add(card := dui.Card().add(dui.Text('!')))
    
    async def add_button_click(button, req: EventRequest):
        row = [randint(0, 10) for i in range(3)]
        table_0.rows = [*table_0.rows, row]
        
        row = [randint(10, 100) for i in range(3)]
        table_1.rows = [*table_1.rows, row]

    async def remove_button_click(button, req: EventRequest):
        table_0.rows = [*table_0.rows[:-1]]
        table_1.rows = [*table_1.rows[:-1]]
    
    # join button
    vflex.add(join := dui.Join())
    join.add(add_button := dui.Button(onclick=add_button_click).add(dui.Text('Add')))
    join.add(edit_button := dui.Button(class_='btn btn-secondary').add(dui.Text('Edit')))
    join.add(remove_button := dui.Button(onclick=remove_button_click, class_='btn btn-primary').add(dui.Text('Remove')))

    # table_0
    header = ['A', 'B', 'C']
    rows = [[j for j in range(i, i + 3)] for i in range(5)]
    vflex.add(table_0 := dui.Table(header=header, rows=rows))
    
    # table_1
    header = ['A', 'B', 'C']
    rows = [[j for j in range(i, i + 3)] for i in range(100, 105)]
    vflex.add(table_1 := dui.Table(header=header, rows=rows))
    return page

def sign_in_page() -> Component:
    page = dui.Page(title='Sign In')
    page.add(navbar := my_navbar())
    return page

def sign_up_page() -> Component:
    page = dui.Page(title='Sign In')
    page.add(navbar := my_navbar())
    return page

g.route('/', root_page())
g.route('/dashboard', dashboard_page())
g.route('/signin', sign_in_page())
g.route('/signup', sign_up_page())
app = g.get_app()

if __name__ == '__main__':
    g.run_app(host='0.0.0.0', port=5000)
