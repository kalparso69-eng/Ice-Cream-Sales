import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

# Load data
df = pd.read_csv('ice-cream.csv')

# Preprocess
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month  # Extract month as number
df['DayOfWeek'] = df['Date'].dt.dayofweek  # Monday=0, Sunday=6

# Features and target
features = ['Temperature', 'Rainfall', 'DayOfWeek', 'Month']
X = df[features]
y = df['IceCreamsSold']

# Handle categorical: DayOfWeek and Month are now numeric, but if needed, encode
# DayOfWeek is already 0-6, Month 1-12

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model: Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'ice_cream_model.pkl')

print("Model trained and saved.")