# gladius
Full-stack web apps in Python

<img src="misc/logo-1.png" alt="WizardLM" style="display: block; margin: auto;" />

**Gladius** aka "gladius" is a **full-stack web framework** facilitating web application development exclusively in pure **Python**, eliminating the need for HTML, CSS, or JavaScript. It is built for those who prefer to use Python, providing access to features typically found in modern web frameworks.

Gladius integrates basic **HTML5** elements, **TailwindCSS** styling, and **DaisyUI** components, built on top of **HTMX**, allowing developers to concentrate on application logic and functionality, while the framework handles the UI/UX aspects. It also incorporates client-side routing typical of Single Page Applications (SPAs), promoting smoother transitions and increased interactivity.

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
