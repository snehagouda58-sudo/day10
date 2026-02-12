import pandas as pd

# Load dataset
df = pd.read_csv("customer_orders.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

print("Columns found:", df.columns)

# Find price column safely
price_col = None
date_col = None

for col in df.columns:
    if col.lower() == 'price':
        price_col = col
    if col.lower() == 'date':
        date_col = col

# Convert Price column
if price_col:
    df[price_col] = df[price_col].astype(str).str.replace('$', '', regex=False)
    df[price_col] = pd.to_numeric(df[price_col], errors='coerce')
else:
    print("Price column not found")

# Convert Date column
if date_col:
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
else:
    print("Date column not found")

# Show results
print("\nData Types:")
print(df.dtypes)

print("\nCleaned Data:")
print(df)

# Average price
if price_col:
    print("\nAverage Price:", df[price_col].mean())


