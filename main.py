import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('Coffee_sales_Analysis/coffee_data.csv')

# Fill missing card values
df['card'] = df['card'].fillna('Unknown')

# Convert date columns
df['date'] = pd.to_datetime(df['date'])
df['datetime'] = pd.to_datetime(df['datetime'])

# -----------------------------
# 1. Total Revenue
# -----------------------------
total_revenue = df['money'].sum()
print(f"Total Revenue: ₹{total_revenue:,.2f}")

# -----------------------------
# 2. Revenue by Coffee Item
# -----------------------------
coffee_revenue = (
    df.groupby('coffee_name')['money']
    .sum()
    .sort_values(ascending=False)
)

print("\nTotal Revenue by Coffee Item:")
print(coffee_revenue)

# -----------------------------
# 3. Top 5 Coffee Items by Revenue
# -----------------------------
plt.figure(figsize=(10, 6))
sns.barplot(
    x=coffee_revenue.head(5).index,
    y=coffee_revenue.head(5).values,
    hue=coffee_revenue.head(5).index,   # differentiate colors
    palette='viridis',
    legend=False
)

plt.title('Top 5 Coffee Items by Revenue')
plt.xlabel('Coffee Name')
plt.ylabel('Revenue (₹)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# 4. Revenue of All Coffee Items
# -----------------------------
plt.figure(figsize=(12, 6))
sns.barplot(
    x=coffee_revenue.index,
    y=coffee_revenue.values,
    hue=coffee_revenue.index,
    palette='Set2',
    legend=False
)

plt.title('Total Revenue Collected by Each Coffee Item')
plt.xlabel('Coffee Name')
plt.ylabel('Revenue (₹)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# 5. Payment Method Distribution
# -----------------------------
payment = df['cash_type'].value_counts()
plt.figure(figsize=(7, 7))
plt.pie(
    payment,
    labels=payment.index,
    autopct='%1.1f%%',
    startangle=90
)
plt.title('Payment Method Distribution')
plt.tight_layout()
plt.show()
