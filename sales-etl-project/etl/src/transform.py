import pandas as pd

def clean_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    # Remove rows with missing values in key columns
    df = df.dropna(subset=["order_id", "product", "quantity", "price"])

    # Convert data types
    df["order_id"] = df["order_id"].astype(int)
    df["quantity"] = df["quantity"].astype(int)
    df["price"] = df["price"].astype(float)

    # Add a computed column for total sales
    df["sales_amount"] = df["quantity"] * df["price"]

    # Ensure order_date is datetime
    df["order_date"] = pd.to_datetime(df["order_date"])

    return df
