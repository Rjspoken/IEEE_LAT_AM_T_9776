# -*- coding: utf-8 -*-
"""Rama_Sr_KNN.ipynb

Automatically generated by Colab.


"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time

df = pd.read_csv('/content/drive/MyDrive/Python/alldataset.csv')
print(df.shape)
df.head()

X = df.iloc[:, :4]
y = df.iloc[:, 4]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Initialize KNN model
knn = KNeighborsRegressor(n_neighbors=5)

# Fit the model
start_time_fit = time.time()
knn.fit(X_train, y_train)
fit_time = time.time() - start_time_fit

# Make predictions
start_time_predict = time.time()
y_pred = knn.predict(X_test)
prediction_time = time.time() - start_time_predict

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r_squared = r2_score(y_test, y_pred)
mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100

print("R-squared:", r_squared)
print("Mean Squared Error (MSE):", mse)
print("Root Mean Squared Error (RMSE):", rmse)
print("Mean Absolute Error (MAE):", mae)
print("Mean Absolute Percentage Error (MAPE):", mape)
print("Fit Time:", fit_time)
print("Prediction Time:", prediction_time)

