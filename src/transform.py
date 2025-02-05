import pandas as pd
from pathlib import Path
from src.ingestion import read_csv_file


def extract_primary_product_id(product_id: str) -> str:
    # This function takes "prod1520#prod100011001100" and returns "prod1520"
    return product_id.split("#")[0]

def add_primary_product_id(df: pd.DataFrame) -> pd.DataFrame:
    # Add a new column 'primaryProductId' by applying the extraction function
    df["primaryProductId"] = df["productId"].apply(extract_primary_product_id)
    return df

def merge_orders_and_inventory(orders_df: pd.DataFrame, inventory_df: pd.DataFrame) -> pd.DataFrame:
    # Transform both DataFrames by adding the 'primaryProductId' column
    orders_df = add_primary_product_id(orders_df)
    inventory_df = add_primary_product_id(inventory_df)
    
    # Save the transformed orders and inventory data for debugging/checking
    orders_df.to_csv("data/processed/orders_transformed.csv", index=False)
    inventory_df.to_csv("data/processed/inventory_transformed.csv", index=False)
    
    # Merge the data on the new column
    merged_df = pd.merge(orders_df, inventory_df, on="primaryProductId", how="left", suffixes=("_order", "_inventory"))
    
    # Save the final merged data
    merged_df.to_csv("data/processed/merged_data.csv", index=False)
    
    return merged_df

if __name__ == "__main__":
    orders_path = Path("data/raw/orders.csv")
    inventory_path = Path("data/raw/inventory.csv")
    
    # Read the raw data
    orders_df = read_csv_file(orders_path)
    inventory_df = read_csv_file(inventory_path)
    
    # Process and merge the data, and save at each step
    merged_df = merge_orders_and_inventory(orders_df, inventory_df)
    
    # Print the merged data (or part of it) so you can see the result
    print("Merged Data Preview:")
    print(merged_df.head())
