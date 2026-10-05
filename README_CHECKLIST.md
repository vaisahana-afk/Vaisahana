# AML Project Summary Checklist

## 1. ML Life Cycle
- Define the problem: detect suspicious AML transactions.
- Collect the transaction dataset.
- Explore and understand the data.
- Clean the dataset.
- Engineer useful features.
- Train a model.
- Evaluate model performance.
- Deploy the model through an API.

## 2. Exploration, Raw Data, and Feature Engineering
- Review raw transaction data and identify issues.
- Check missing values, duplicates, and invalid entries.
- Clean country codes and amount values.
- Convert labels into numeric values.
- Prepare features for training.

## 3. ML Algorithm Explanation
- A classification algorithm such as Logistic Regression, Random Forest, or XGBoost can be used.
- These algorithms learn patterns from historical transaction data.
- The model predicts whether a new transaction is suspicious or normal.
- Precision and recall are important because AML false negatives are costly.

## 4. Colab or IDE
- This project can be developed in Google Colab or in a local IDE.
- The current project is built in VS Code.

## 5. Project Environment
- Python is used for data processing and model development.
- FastAPI is used for deployment.
- Pandas is used for data handling.
- Libraries are listed in requirements.txt.

## 6. Project Files
- main.py: API application
- prepare_data.py: data cleaning and preprocessing
- data/raw_transactions.csv: raw dataset
- data/cleaned_transactions.csv: cleaned dataset
- requirements.txt: dependencies
- api_test.http: sample request for testing

## 7. Final Note
- This project demonstrates a complete ML workflow from data preparation to deployment.
- The API is ready to accept transaction data and return a suspicious/normal prediction.
