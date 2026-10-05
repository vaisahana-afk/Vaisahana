import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# For this AML task, use LogisticRegression (classification), not LinearRegression.
df = pd.read_csv("data/raw_transactions.csv")

df = df[df["is_suspicious"].notna()].copy()
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

# Convert target values to 0/1
label_map = {
    "true": 1,
    "false": 0,
    "1": 1,
    "0": 0,
    "suspicious": 1,
    "normal": 0,
}
df["is_suspicious"] = df["is_suspicious"].astype(str).str.strip().str.lower().map(label_map)
df = df.dropna(subset=["amount", "is_suspicious"]).copy()

X = df[["amount"]]
y = df["is_suspicious"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, predictions))

joblib.dump(model, "aml_model.pkl")
print("Model saved as aml_model.pkl")
