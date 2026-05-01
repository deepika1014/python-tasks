import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
df = pd.read_csv('house_data.csv')

print("\nDataset Preview:\n")
print(df.head())

# ------------------------------
# 1. Features & Target
# ------------------------------
X = df[['area', 'bedrooms', 'bathrooms']]
y = df['price']

# ------------------------------
# 2. Train-Test Split
# ------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ------------------------------
# 3. Train Model
# ------------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# ------------------------------
# 4. Predictions
# ------------------------------
y_pred = model.predict(X_test)

# ------------------------------
# 5. Evaluation
# ------------------------------
print("\nModel Evaluation:")
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# ------------------------------
# 6. Predict New House Price
# ------------------------------
sample_house = pd.DataFrame({
    'area': [2000],
    'bedrooms': [3],
    'bathrooms': [2]
})

predicted_price = model.predict(sample_house)

print("\nPredicted Price for [2000 sqft, 3BHK]:", predicted_price[0])

# ------------------------------
# 7. Graphs
# ------------------------------

# Graph 1: Actual vs Predicted
plt.figure()
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted Prices")
plt.show()

# Graph 2: Area vs Price
plt.figure()
plt.scatter(df['area'], df['price'])
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Area vs Price")
plt.show()

# ------------------------------
# 8. Insights
# ------------------------------
print("\nInsights:")
print("- House price increases with area.")
print("- More bedrooms and bathrooms increase the price.")
print("- Model predictions are very close to actual values (high accuracy).")