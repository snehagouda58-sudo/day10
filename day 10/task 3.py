import pandas as pd

# Load dataset
df = pd.read_csv("customer_orders.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

print("Columns found:", df.columns)

# Find Location column safely
location_col = None

for col in df.columns:
    if col.lower() == 'location':
        location_col = col

# Check before cleaning
if location_col:
    print("\nBefore cleaning:")
    print(df[location_col].unique())

    # Clean the Location column
    df[location_col] = df[location_col].astype(str).str.strip().str.title()

    print("\nAfter cleaning:")
    print(df[location_col].unique())

else:
    print("Location column not found in CSV file")

# Show cleaned data
print("\nCleaned Data:")
print(df)
