from random import randint

from gladius import Gladius, Component, EventRequest
from gladius.daisyui import DaisyUI

g = Gladius()
ui = DaisyUI(g)

def MyNavbar() -> Component:
    navbar = ui.Navbar(hx_boost='true')
    navbar.add(a := ui.Link(href='/').add('Home'))
    navbar.add(a := ui.Link(href='/dashboard').add('Dashboard'))
    navbar.add(a := ui.Link(href='/signin').add('Sign In'))
    navbar.add(a := ui.Link(href='/signup').add('Sign Up'))
    return navbar

def MyJoin() -> Component:
    join = ui.Join(hx_boost='true')
    join.add(a := ui.Link(class_='btn join-item', href='/').add('Home'))
    join.add(a := ui.Link(class_='btn join-item', href='/dashboard').add('Dashboard'))
    join.add(a := ui.Link(class_='btn join-item', href='/signin').add('Sign In'))
    join.add(a := ui.Link(class_='btn join-item', href='/signup').add('Sign Up'))
    return join

def RootPage() -> Component:
    # root/index
    page = ui.Page(title='TangledLabs')

    # navbar
    page.add(navbar := MyNavbar())

    # join buttons
    page.add(flex := ui.Flex())
    flex.add(join := MyJoin())
    return page

def DashboardPage() -> Component:
    page = ui.Page(title='Dashboard')
    page.add(navbar := MyNavbar())
    
    # vflex - Hello World
    page.add(vflex := ui.VFlex())
    vflex.add(card := ui.Card().add('Hello'))
    vflex.add(flex := ui.Flex())
    flex.add(card := ui.Card().add('World'))
    flex.add(card := ui.Card().add('!'))
    
    async def add_button_click(button, req: EventRequest):
        row = [randint(0, 10) for i in range(3)]
        table_0.rows = [*table_0.rows, row]
        
        row = [randint(10, 100) for i in range(3)]
        table_1.rows = [*table_1.rows, row]

    async def remove_button_click(button, req: EventRequest):
        table_0.rows = [*table_0.rows[:-1]]
        table_1.rows = [*table_1.rows[:-1]]
    
    # join button
    vflex.add(join := ui.Join())
    join.add(add_button := ui.Button(onclick=add_button_click).add('Add'))
    join.add(edit_button := ui.Button(class_='btn btn-secondary').add('Edit'))
    join.add(remove_button := ui.Button(onclick=remove_button_click, class_='btn btn-primary').add('Remove'))

    # table_0
    header = ['A', 'B', 'C']
    rows = [[j for j in range(i, i + 3)] for i in range(5)]
    vflex.add(table_0 := ui.Table(header=header, rows=rows))
    
    # table_1
    header = ['A', 'B', 'C']
    rows = [[j for j in range(i, i + 3)] for i in range(100, 105)]
    vflex.add(table_1 := ui.Table(header=header, rows=rows))
    return page

def SignInPage() -> Component:
    page = ui.Page(title='Sign In')
    page.add(navbar := MyNavbar())
    return page

def SignUpPage() -> Component:
    page = ui.Page(title='Sign In')
    page.add(navbar := MyNavbar())
    return page

g.route('/', RootPage())
g.route('/dashboard', DashboardPage())
g.route('/signin', SignInPage())
g.route('/signup', SignUpPage())
app = g.get_app()

if __name__ == '__main__':
    g.run_app(host='0.0.0.0', port=5000)
