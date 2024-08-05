import pandas as pd
import matplotlib.pyplot as plt


# Load the data from the CSV file
data = pd.read_csv('product_n.csv')

# Data cleaning for 'Price'
data['Price'] = data['Price'].str.replace('$', '').astype(float)


# Convert 'Manufacturing Date' and 'Expiry Date' to datetime
data['Manufacturing Date'] = pd.to_datetime(data['Manufacturing Date'])
data['Expiry Date'] = pd.to_datetime(data['Expiry Date'])


# Visualization: Price Distribution (Histogram)
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)  # 1 row, 2 columns, 1st subplot
plt.hist(data['Price'], bins=15, color='skyblue', edgecolor='black')


plt.title('Distribution of Product Prices')
plt.xlabel('Price ($)')
plt.ylabel('Frequency')
plt.grid(True)


plt.tight_layout()
plt.show()
