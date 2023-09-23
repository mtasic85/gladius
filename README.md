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

<img src="misc/logo-1.png" style="display: block; margin: auto;" />

**Gladius** aka "gladius" is a **full-stack web framework** facilitating web application development exclusively in pure **Python**, eliminating the need for HTML, CSS, or JavaScript. It is built for those who prefer to use Python, providing access to features typically found in modern web frameworks.

Gladius integrates basic **HTML5** elements, **TailwindCSS** styling, and **DaisyUI** components, built on top of **aiohttp**, **uvloop**, and **HTMX**, allowing developers to concentrate on application logic and functionality, while the framework handles the UI/UX aspects. It also incorporates client-side routing typical of Single Page Applications (SPAs), promoting smoother transitions and increased interactivity.

In essence, gladius offers a simplified and cohesive development experience, making it a practical choice for developers seeking a Python-centric approach to both frontend and backend development.

## Install
```bash
pip install gladius
```

## Run Examples
```bash
python -m venv venv
source venv/bin/activate
gunicorn app:app --reload --bind '0.0.0.0:5000' --worker-class aiohttp.GunicornWebWorker
```
