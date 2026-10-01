from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="FastAPI Quickstart")


class Message(BaseModel):
    text: str


class AMLTransaction(BaseModel):
    transaction_id: str
    amount: float
    source_country: str
    destination_country: str


@app.get("/")
def home():
    return {"message": "Your FastAPI app is running!"}


@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello, {name}!"}


@app.post("/messages")
def create_message(message: Message):
    return {"received": message.text}


@app.post("/predict")
def predict_transaction(transaction: AMLTransaction):
    country_names = {
        "SG": "Singapore",
        "AE": "United Arab Emirates",
    }

    is_suspicious = (
        transaction.amount > 10000
        and transaction.source_country != transaction.destination_country
    )

    payload = {
        "transaction_id": transaction.transaction_id,
        "amount": transaction.amount,
        "source_country": transaction.source_country,
        "source_country_name": country_names.get(transaction.source_country, transaction.source_country),
        "destination_country": transaction.destination_country,
        "destination_country_name": country_names.get(transaction.destination_country, transaction.destination_country),
        "is_suspicious": is_suspicious,
        "status": "flagged" if is_suspicious else "normal",
    }

    if transaction.source_country == "SG":
        payload["risk_note"] = "Singapore outbound transfer pattern detected."
        payload["country_context"] = {
            "origin": "Singapore",
            "destination": payload["destination_country_name"],
            "related_alert": "Review for higher AML scrutiny."
        }

    return payload