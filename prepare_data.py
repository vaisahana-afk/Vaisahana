from pathlib import Path

import pandas as pd


DATA_DIR = Path(__file__).parent / "data"
RAW_DATA_PATH = DATA_DIR / "raw_transactions.csv"
CLEAN_DATA_PATH = DATA_DIR / "cleaned_transactions.csv"
REQUIRED_COLUMNS = [
    "transaction_id",
    "amount",
    "source_country",
    "destination_country",
    "transaction_date",
    "is_suspicious",
]


def main():
    raw = pd.read_csv(RAW_DATA_PATH)
    missing_columns = set(REQUIRED_COLUMNS) - set(raw.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(sorted(missing_columns))}")

    print("Raw data overview")
    print(f"Rows: {len(raw)}")
    print(f"Columns: {', '.join(raw.columns)}")
    print("Missing values by column:")
    print(raw[REQUIRED_COLUMNS].isna().sum().to_string())
    print(f"Duplicate transaction IDs: {raw['transaction_id'].duplicated().sum()}")
    print("Raw amount statistics:")
    print(pd.to_numeric(raw["amount"], errors="coerce").describe().to_string())

    cleaned = raw[REQUIRED_COLUMNS].copy()
    for column in ("transaction_id", "source_country", "destination_country"):
        cleaned[column] = cleaned[column].astype("string").str.strip()

    cleaned["source_country"] = cleaned["source_country"].str.upper()
    cleaned["destination_country"] = cleaned["destination_country"].str.upper()
    cleaned["amount"] = pd.to_numeric(cleaned["amount"], errors="coerce")
    cleaned["transaction_date"] = pd.to_datetime(
        cleaned["transaction_date"], errors="coerce", utc=True
    )

    label_values = cleaned["is_suspicious"].astype("string").str.strip().str.lower()
    cleaned["is_suspicious"] = label_values.map(
        {"true": 1, "false": 0, "1": 1, "0": 0, "suspicious": 1, "normal": 0}
    )

    row_count_before_cleaning = len(cleaned)
    cleaned = cleaned.dropna(subset=REQUIRED_COLUMNS)
    cleaned = cleaned[
        (cleaned["transaction_id"] != "")
        & (cleaned["source_country"] != "")
        & (cleaned["destination_country"] != "")
        & (cleaned["amount"] > 0)
    ]
    cleaned = cleaned.drop_duplicates(subset="transaction_id", keep="first")
    cleaned["is_suspicious"] = cleaned["is_suspicious"].astype("int64")
    cleaned["transaction_date"] = cleaned["transaction_date"].dt.strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )

    DATA_DIR.mkdir(exist_ok=True)
    cleaned.to_csv(CLEAN_DATA_PATH, index=False)

    print("\nCleaning summary")
    print(f"Rows before cleaning: {row_count_before_cleaning}")
    print(f"Rows after cleaning: {len(cleaned)}")
    print(f"Rows removed: {row_count_before_cleaning - len(cleaned)}")
    print(f"Cleaned data written to: {CLEAN_DATA_PATH.relative_to(Path(__file__).parent)}")
    print("Cleaned label counts:")
    print(cleaned["is_suspicious"].value_counts().sort_index().to_string())


if __name__ == "__main__":
    main()