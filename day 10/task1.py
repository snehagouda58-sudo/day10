import pandas as pd

try:
    # Load dataset (use full path if needed)
    df = pd.read_csv("customer_orders.csv")

    # Shape before cleaning
    print("Shape BEFORE cleaning:", df.shape)

    # 1. Missing values report
    print("\nMissing values report:")
    print(df.isna().sum())

    # 2. Fill missing numeric values with median
    numeric_cols = df.select_dtypes(include='number').columns

    for col in numeric_cols:
        median_value = df[col].median()
        df[col] = df[col].fillna(median_value)

    # 3. Remove duplicate rows
    df = df.drop_duplicates()

    # 4. Shape after cleaning
    print("\nShape AFTER cleaning:", df.shape)

    # Show cleaned data
    print("\nCleaned Data:")
    print(df.head())

except FileNotFoundError:
    print("Error: customer_orders.csv file not found. Check file location.")

except pd.errors.EmptyDataError:
    print("Error: customer_orders.csv file is empty. Please add data.")

except Exception as e:
    print("Unexpected error:", e)
