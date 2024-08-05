import pandas as pd

# Load the data
file_path = 'website access.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the dataframe
print("First few rows of the original data:")
print(df.head())

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Handle missing values
# Fill missing numerical values with the mean
df.fillna(df.mean(numeric_only=True), inplace=True)

# Fill missing categorical values with the mode
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# Convert Access Date to datetime
df['Access Date'] = pd.to_datetime(df['Access Date'])

# Convert Conversion Rate and Bounce Rate to numeric values (without %)
df['Conversion Rate'] = df['Conversion Rate'].str.rstrip('%').astype(float) / 100
df['Bounce Rate'] = df['Bounce Rate'].str.rstrip('%').astype(float) / 100

# Convert Session Duration to total minutes
df['Session Duration'] = df['Session Duration'].apply(lambda x: int(x.split()[0]))

# Describe the numerical columns to find any outliers
numerical_summary = df.describe()

# Check for any duplicate rows
duplicates = df.duplicated().sum()

# Print summary statistics and number of duplicate rows
print("\nSummary statistics of numerical columns:")
print(numerical_summary)
print(f'\nNumber of duplicate rows: {duplicates}')

# Drop duplicate rows if any
if duplicates > 0:
    df = df.drop_duplicates()

# Save the cleaned data to a new CSV file
cleaned_file_path = 'cleaned_website_access.csv'
df.to_csv(cleaned_file_path, index=False)

print(f"\nCleaned data saved to {cleaned_file_path}")
