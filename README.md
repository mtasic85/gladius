# gladius
Full-stack web apps in Python

## Install
```bash
pip install swordfish
```

## Run Examples
```bash
python -m venv venv
source venv/bin/activate
gunicorn app:app --reload --bind '0.0.0.0:5000' --worker-class aiohttp.GunicornWebWorker
```
