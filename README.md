# FastAPI Quickstart

A small Python API to learn the basics: routes, path parameters, and request-body validation.

## Run it

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
fastapi dev main.py
```

Open <http://127.0.0.1:8000/docs> to try each endpoint in your browser.

- `GET /` returns a welcome message.
- `GET /hello/{name}` uses a value from the URL, for example `/hello/Ada`.
- `POST /messages` accepts JSON such as `{"text":"Learning FastAPI"}`.

FastAPI validates the `POST` body and builds the interactive API docs from the Python types.
