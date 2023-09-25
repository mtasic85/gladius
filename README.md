# gladius

<!--
[![Build][build-image]]()
[![Status][status-image]][pypi-project-url]
[![Stable Version][stable-ver-image]][pypi-project-url]
[![Coverage][coverage-image]]()
[![Python][python-ver-image]][pypi-project-url]
[![License][mit-image]][mit-url]
-->
[![Downloads](https://img.shields.io/pypi/dm/gladius)](https://pypistats.org/packages/gladius)
[![Supported Versions](https://img.shields.io/pypi/pyversions/gladius)](https://pypi.org/project/gladius)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

<img src="https://github.com/mtasic85/gladius/raw/main/misc/logo-1.png" alt="" style="display: block; margin: auto;" />

**Gladius** aka "gladius" is a **full-stack web framework** facilitating web application development exclusively in pure **Python**, eliminating the need for HTML, CSS, or JavaScript. It is built for those who prefer to use Python, providing access to features typically found in modern web frameworks.

Gladius integrates basic **HTML5** elements, **TailwindCSS** styling, and **DaisyUI** components, built on top of **aiohttp**, **uvloop**, and **htmx**, allowing developers to concentrate on application logic and functionality, while the framework handles the UI/UX aspects. It also incorporates client-side routing typical of Single Page Applications (SPAs), promoting smoother transitions and increased interactivity.

In essence, gladius offers a simplified and cohesive development experience, making it a practical choice for developers seeking a Python-centric approach to both frontend and backend development.

## Hello World

```python
from random import randint

from gladius import Gladius, Component, Event
from gladius.daisyui import DaisyUI

# glados daisyui
g = Gladius()
dui = DaisyUI(g)

# callbacks
async def hello_button_click(button: Component, event: Event):
    hello_text.content = f'Hello {randint(0, 100)}'

async def world_button_click(button: Component, event: Event):
    world_text.content = f'World {randint(0, 100)}'

# page
page = dui.Page(title='Hello world 0', class_='p-10')
page.add(vflex := dui.VFlex())

# top cards
vflex.add(card := dui.Card())
card.add(hello_text := dui.Text('Hello'))

vflex.add(card := dui.Card())
card.add(world_text := dui.Text('World'))

# buttons
vflex.add(hflex := dui.Flex())
hflex.add(join := dui.Join())
join.add(button := dui.Button(class_='btn btn-primary', onclick=hello_button_click))
button.add(text := dui.Text('Hello'))
join.add(button := dui.Button(class_='btn btn-success', onclick=world_button_click))
button.add(text := dui.Text('World'))

# router
g.route('/', page)
app = g.get_app()

if __name__ == '__main__':
    g.run_app(host='0.0.0.0', port=5000)
```

## Install
```bash
pip install gladius
```

## Run Examples

```bash
git clone https://github.com/mtasic85/gladius.git
cd gladius
python -m venv venv
source venv/bin/activate
pip install
```

Hello world:

```bash
gunicorn examples.hello_world_0:app --reload --bind '0.0.0.0:5000' --worker-class aiohttp.GunicornWebWorker
```

Multi-page:

```bash
gunicorn examples.multi_page_0:app --reload --bind '0.0.0.0:5000' --worker-class aiohttp.GunicornWebWorker
```