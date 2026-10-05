import numpy as np
from sklearn.linear_model import LinearRegression

# 1. Dummy training data matching your transaction context
# Features layout: [amount, source_is_SG (1 or 0), dest_is_AE (1 or 0)]
X_train = np.array([
    [1000.0,  1, 0],
    [5000.0,  0, 1],
    [12000.0, 1, 1],
    [25000.0, 1, 0],
    [3000.0,  0, 0]
])

# Target labels (Historical risk scores that train the model)
y_train = np.array([0.1, 0.3, 0.85, 0.9, 0.15])

# 2. Initialize and train the Linear Regression framework
regression_model = LinearRegression()
regression_model.fit(X_train, y_train)

# This confirmation prints to your terminal when the server boots up
print("INFO: Linear Regression model trained and initialized successfully.")
