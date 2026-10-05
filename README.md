<<<<<<< HEAD
# AML Transaction API

A small learning project for exploring and preparing transaction data, then serving AML predictions with FastAPI.
=======
# FastAPI Quickstart

A small Python API to learn the basics: routes, path parameters, and request-body validation.
>>>>>>> 47296a4e2a4079faf242d0b335cabd738ad7fbae

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
<<<<<<< HEAD

## Explore and clean the sample data

The included `data/raw_transactions.csv` is synthetic practice data, not real customer or financial data. It includes a few intentional data-quality issues so the preparation script has something to find.

```bash
python prepare_data.py
```

The script prints a raw-data summary and writes `data/cleaned_transactions.csv`. It trims and normalizes text fields, converts amounts and labels to consistent types, removes duplicate transaction IDs, and excludes rows with missing or invalid required values. Review the output summary before using the cleaned data for modeling.

This preparation workflow is separate from the current `/predict` endpoint, which still uses a demonstration rule rather than a trained ML model.
=======
>>>>>>> 47296a4e2a4079faf242d0b335cabd738ad7fbae
