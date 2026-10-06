from io import StringIO
import traceback
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import numpy as np
import model

# 1. Initialize the app ONLY ONCE
app = FastAPI(title="FastAPI Quickstart")

# 2. Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Data Models
class Message(BaseModel):
    text: str

class AMLTransaction(BaseModel):
    transaction_id: str
    amount: float
    source_country: str
    destination_country: str

class RawAMLTransaction(BaseModel):
    transaction_id: str | None = None
    amount: float = 0.0
    source_country: str | None = None
    destination_country: str | None = None

class RegressionInput(BaseModel):
    features: list[float]

# 4. Standard Routes
@app.get("/")
def home():
    return {"message": "Your FastAPI app is running!"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello, {name}!"}

@app.post("/messages")
def create_message(message: Message):
    return {"received": message.text}

# 5. Combined Single /predict Route
@app.post("/predict")
def predict_transaction(transaction: AMLTransaction):
    try:
        country_names = {
            "SG": "Singapore",
            "AE": "United Arab Emirates",
        }
        is_suspicious = (transaction.amount > 10000 and transaction.source_country != transaction.destination_country)
        
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
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/predict_raw")
def predict_raw_transaction(transaction: RawAMLTransaction):
    try:
        src = str(transaction.source_country or "").upper()
        dest = str(transaction.destination_country or "").upper()
        amt = transaction.amount or 0.0
        is_suspicious = (amt > 10000 and src != dest)
        return {
            "transaction_id": transaction.transaction_id,
            "amount": amt,
            "source_country": transaction.source_country,
            "destination_country": transaction.destination_country,
            "is_suspicious": is_suspicious,
            "status": "flagged" if is_suspicious else "normal",
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 6. ML Regression Route
@app.post("/predict_regression")
def predict_regression(data: RegressionInput):
    try:
        input_matrix = np.array(data.features).reshape(1, -1)
        raw_prediction = model.regression_model.predict(input_matrix)
        prediction = float(raw_prediction[0])
        
        if prediction > 0.50:
            verdict = "High Risk - Flagged for AML Scrutiny"
        elif prediction > 0.30:
            verdict = "Medium Risk - Review Recommended"
        else:
            verdict = "Low Risk - Safe Transaction"
        
        return {
            "status": "success",
            "prediction_score": round(prediction, 4),
            "risk_percentage": f"{round(prediction * 100, 2)}%",
            "final_verdict": verdict
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Regression Error: {str(e)}")

# 7. CSV Upload Route
@app.post("/upload_raw_csv")
async def upload_raw_csv(file: UploadFile = File(...)):
    try:
        content = await file.read()
        df = pd.read_csv(StringIO(content.decode("utf-8")))
        preview = []
        for _, row in df.head(10).iterrows():
            preview.append({
                "transaction_id": row.get("transaction_id"),
                "amount": row.get("amount"),
                "status": "processed"
            })
        return {"rows_read": len(df), "preview": preview}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
