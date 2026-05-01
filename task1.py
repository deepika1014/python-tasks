import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('task1_dataset.csv')

print("\nDataset Preview:\n")
print(df.head())

print("\nBasic Statistics:\n")
numeric_cols = df.select_dtypes(include=['number'])

for col in numeric_cols.columns:
    print(f"Average of {col}: {df[col].mean():.2f}")

plt.figure()
plt.bar(df['City'], df['Sales'])
plt.title('Sales by City')
plt.xlabel('City')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure()
plt.scatter(df['Sales'], df['Profit'])
plt.title('Sales vs Profit')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.tight_layout()
plt.show()

plt.figure()
sns.heatmap(numeric_cols.corr(), annot=True)
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()

print("\nInsights:")
print("- Sales are highest in cities like Delhi and Bangalore.")
print("- Profit increases as sales increase (positive correlation).")
print("- Expenses are directly related to sales.")
print("- Higher sales cities generate higher profits.")