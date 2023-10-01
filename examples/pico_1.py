from random import randint

from gladius import Gladius, Component, Event
from gladius.html5 import Html5
from gladius.pico import Pico

g = Gladius()
h = Html5(g)
p = Pico(g)

# Page
page = p.Page(title='Pico.css - 1')

page.add(main := p.Main(class_='container'))
main.add(grid := p.Grid(id='grid'))

# sidebar
grid.add(aside := p.Aside())

# new chat button
aside.add(a := p.Button(class_='outline'))
a.add(t := p.Text('''
    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6" width=24 height=24>
        <path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15" />
    </svg>
'''))

a.add(t := p.Text('New Chat'))

# chats
chats = [{'id': i, 'title': f'Chat {i}'} for i in range(10)]

for chat in chats:
    aside.add(a := p.Button(class_='secondary outline'))

    a.add(t := p.Text('''
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6" widthh=24 height=24>
            <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12.76c0 1.6 1.123 2.994 2.707 3.227 1.087.16 2.185.283 3.293.369V21l4.076-4.076a1.526 1.526 0 011.037-.443 48.282 48.282 0 005.68-.494c1.584-.233 2.707-1.626 2.707-3.228V6.741c0-1.602-1.123-2.995-2.707-3.228A48.394 48.394 0 0012 3c-2.392 0-4.744.175-7.043.513C3.373 3.746 2.25 5.14 2.25 6.741v6.018z" />
        </svg>
    '''))

    a.add(t := p.Text(chat['title']))

# main
grid.add(section := p.Section())
section.add(h1 := p.H1('Chat'))


# router
g.route('/', page)
app = g.get_app()

if __name__ == '__main__':
    g.run_app(host='0.0.0.0', port=5000)
