# AML Transaction Classification: From Raw Data to Predictions

Slide-ready outline for presenting the project step by step. The notes distinguish implemented features from planned machine-learning work.

## Slide 1: Project Goal

- Goal: classify a transaction as suspicious or normal.
- This is a supervised binary classification problem.
- Historical transactions provide the examples and labels used for training.
- The intended result is a prediction for a new transaction.

Speaker note: The included CSV is synthetic practice data, not real customer or financial data.

## Slide 2: Machine-Learning Lifecycle

1. Define the problem.
2. Collect and inspect raw data.
3. Clean invalid or inconsistent records.
4. Engineer features for the algorithm.
5. Split labeled data into training and evaluation sets.
6. Train a model and evaluate its results.
7. Use the trained model for batch or API predictions.
8. Monitor and improve it as more labeled data becomes available.

## Slide 3: Explore the Raw Data

- Input file: `data/raw_transactions.csv`.
- Fields: transaction ID, amount, source country, destination country, date, and suspicious label.
- The sample has 14 raw rows and intentionally includes data-quality problems.
- Examples include a missing amount, non-numeric amount, invalid date, duplicate ID, inconsistent country-code casing, and mixed label formats.
- `prepare_data.py` reports missing values, duplicate IDs, and amount statistics.

## Slide 4: Clean the Data

- Run `python prepare_data.py` from the project folder.
- The script checks required columns and stops if any are missing.
- It trims text, standardizes country codes, converts amounts and dates, and maps labels to 1 or 0.
- It removes rows with missing or invalid required values, non-positive amounts, blank key fields, or duplicate transaction IDs.
- Output file: `data/cleaned_transactions.csv`.
- In the current sample, 14 raw rows become 9 cleaned rows.

Speaker note: This data-cleaning step is implemented. It does not train a model.

## Slide 5: Define Features and the Target

- Target (`y`): `is_suspicious`, where 1 means suspicious and 0 means normal.
- Candidate numeric features: amount, transaction month, and day of week.
- Candidate categorical features: source country and destination country.
- Derived feature example: whether source and destination countries are the same.
- Do not use `transaction_id` as a model feature.
- Do not include `is_suspicious` in the input features; that would leak the answer.

Speaker note: Country codes need encoding, such as one-hot encoding. Numeric values may need scaling depending on the algorithm.

## Slide 6: Split Data Before Training

- Separate input features from the target label.
- Split labeled records into training data and held-out evaluation data.
- Fit preprocessing only on the training split, then apply the fitted transformations to evaluation data.
- Never evaluate a model only on the same rows it trained on.
- The current 9 cleaned rows are too few for a trustworthy train/test evaluation.

Speaker note: More correctly labeled examples are needed before reported performance can be meaningful. A tiny sample is useful for demonstrating code flow, not for claiming model quality.

## Slide 7: Choose and Explain an Algorithm

- Start with Logistic Regression as a simple classification baseline.
- It estimates how input features relate to the probability of a transaction being suspicious.
- Compare with Random Forest once there is enough labeled data; it can learn non-linear patterns but is less straightforward to explain.
- Choose based on held-out evaluation results, not on training accuracy alone.

Speaker note: No trained algorithm has been selected or implemented in this project yet.

## Slide 8: Evaluate the Model

- Confusion matrix: counts correct and incorrect suspicious/normal predictions.
- Precision: of transactions flagged suspicious, how many were actually suspicious?
- Recall: of actually suspicious transactions, how many did the model catch?
- F1-score: combines precision and recall into one measure.
- In AML, missing suspicious transactions is costly, but excessive false alarms also create review workload.

Speaker note: Report these metrics on held-out data and include the number of evaluation examples. Do not claim reliable performance from the current 9 cleaned rows.

## Slide 9: Predict Transactions

- Batch workflow: read new transaction rows, apply the same cleaning and feature transformations, predict, and write results to an output CSV.
- API workflow: send one transaction to FastAPI and return its predicted class (and, if configured, a probability score).
- The prediction input must have the same feature fields and transformations used during training.
- The current `/predict` endpoint accepts one JSON transaction and uses a hand-written demo rule.
- It does not load a trained model or automatically read either CSV.

## Slide 10: Development Environment and Project Files

- IDE: VS Code. Google Colab is an alternative notebook environment.
- Python environment and dependencies are managed locally with a virtual environment and `requirements.txt`.
- `prepare_data.py`: implemented data checks and cleaning.
- `main.py`: FastAPI app with a demonstration rule, not trained-model inference.
- `data/raw_transactions.csv`: synthetic raw input.
- `data/cleaned_transactions.csv`: generated cleaned output.
- `requirements.txt` currently lists FastAPI and Pandas. Model training will also need an ML library such as scikit-learn.

PowerShell setup and cleaning commands:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python prepare_data.py
```

## Slide 11: Current Status and Next Steps

Implemented:

- Synthetic raw transaction sample.
- Data exploration and cleaning script.
- Cleaned CSV output.
- FastAPI endpoint with a demonstration prediction rule.

Still needed for a real ML workflow:

- Obtain substantially more accurately labeled transactions.
- Add feature engineering and a reproducible training/evaluation pipeline.
- Compare algorithms using held-out precision, recall, and F1-score.
- Save the fitted preprocessing-and-model pipeline.
- Add batch CSV predictions and connect FastAPI to the saved model.

Closing message: The project currently demonstrates raw-data preparation and a basic API. Training, evaluating, and deploying a machine-learning model are the next development steps.