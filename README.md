# gladius
Full-stack web apps in Python

<img src="misc/logo-1.png" alt="WizardLM" style="display: block; margin: auto;" />

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
