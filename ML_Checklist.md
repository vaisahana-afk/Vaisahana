# AML ML Project Checklist

## 1. ML Life Cycle
- Problem definition: detect suspicious financial transactions.
- Data collection: use transaction data from the raw dataset.
- Data exploration: analyze rows, columns, missing values, duplicates, and patterns.
- Data cleaning: remove invalid or inconsistent records.
- Feature engineering: convert fields into usable ML features.
- Model training: train a classification model.
- Evaluation: measure accuracy, precision, recall, and F1-score.
- Deployment: expose the model using FastAPI.

## 2. Exploration, Raw Data, Feature Engineering, and Model
- Explore the raw transaction data to understand the structure.
- Check missing values, duplicate transaction IDs, and invalid amounts.
- Clean the dataset before training.
- Convert amount to numeric values.
- Standardize country codes and transaction dates.
- Encode categorical variables for model input.
- Train a classification algorithm to detect suspicious transactions.

## 3. ML Algorithm Explanation
- A classification model such as Logistic Regression, Random Forest, or XGBoost can be used.
- These algorithms work well for tabular transaction data.
- The model learns patterns from past transactions and predicts whether a new transaction is suspicious.
- Evaluation metrics such as precision and recall are important in AML because false negatives are costly.

## 4. Colab or IDE
- Project can be developed in Google Colab or in a local IDE such as VS Code.
- This project is currently developed in VS Code.
- The environment is managed using Python and a virtual environment.

## 5. Project Environment
- Python is used for data processing and model building.
- FastAPI is used to deploy the prediction service.
- Pandas is used for data preprocessing.
- The required libraries are listed in requirements.txt.
- The project files include:
  - main.py
  - prepare_data.py
  - data/raw_transactions.csv
  - data/cleaned_transactions.csv
  - requirements.txt

## 6. Final Project Summary
- This project follows the full ML lifecycle from raw data to model use.
- The cleaned dataset is prepared for ML training.
- The trained model can be exposed through an API endpoint for real-time transactions.
- The project demonstrates both data science and deployment skills.
