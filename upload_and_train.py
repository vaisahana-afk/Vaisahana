import pandas as pd
import numpy as np
from pathlib import Path
import model

def train_model_from_csv(file_path):
    print(f"Opening data file: {file_path}")
    try:
        df = pd.read_csv(file_path)
        
        X_data = []
        y_data = []
        
        for _, row in df.iterrows():
            amount_raw = row.get("amount")
            
            # Skip rows where amount is completely blank or missing (NaN)
            if pd.isna(amount_raw):
                continue
                
            try:
                amt = float(amount_raw)
                # Skip negative or invalid numeric anomalies
                if np.isnan(amt) or np.isinf(amt):
                    continue
            except (ValueError, TypeError):
                # Skip row if amount contains text letters instead of a clean number
                continue
                
            is_sg = 1 if str(row.get("source_country", "")).strip().upper() == "SG" else 0
            is_ae = 1 if str(row.get("destination_country", "")).strip().upper() == "AE" else 0
            
            # Logical target tagging rules for regression tracking
            risk_score = 0.85 if (amt > 10000 and is_sg and is_ae) else 0.15
            
            X_data.append([amt, is_sg, is_ae])
            y_data.append(risk_score)
            
        # Ensure we actually found valid non-empty numeric data rows to train on
        if len(X_data) == 0:
            print("❌ ERROR: No valid numerical data rows found in the CSV file to train on!")
            return
            
        model.regression_model.fit(X_data, y_data)
        
        print("\n====================================================")
        print("🎉 SUCCESS: AI TRAINING FROM DISK COMPLETE!")
        print("====================================================")
        print(f"Valid Rows Processed: {len(X_data)} (Skipped bad/empty rows)")
        print(f"New Intercept Baseline: {model.regression_model.intercept_:.4f}")
        print(f"New Weight Multipliers: {model.regression_model.coef_}")
        print("====================================================\n")
        
    except Exception as e:
        print(f"Error parsing data file: {str(e)}")

if __name__ == "__main__":
    script_directory = Path(__file__).parent
    target_csv = script_directory / "data" / "raw_transactions.csv"
    train_model_from_csv(target_csv)




