# src/transform.py

import pandas as pd
from pathlib import Path
from typing import Tuple
from ingestion import read_csv_file  

# Set Pandas to show all columns and rows when printing DataFrames.
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

def extract_primary_product_id(product_id: str) -> str:
    """
    Takes a product ID that comes in a format like "prod1520#prod100011001100"
    and returns just the first part, e.g., "prod1520".
    """
    return product_id.split("#")[0]

def add_primary_product_id(df: pd.DataFrame, id_column: str = "productId") -> pd.DataFrame:
    """
    Adds a new column called 'primaryProductId' to the DataFrame.
    This new column contains only the basic product ID (the part before the '#' sign).
    """
    df["primaryProductId"] = df[id_column].apply(extract_primary_product_id)
    return df

def merge_orders_and_inventory(orders_df: pd.DataFrame, inventory_df: pd.DataFrame) -> pd.DataFrame:
    """
    Combines the orders and inventory data by matching on the basic product ID.
    First, it adds a 'primaryProductId' column to both DataFrames, then it merges them
    using that column. The merge uses a left join so that all orders are kept.
    """
    orders_df = add_primary_product_id(orders_df, "productId")
    inventory_df = add_primary_product_id(inventory_df, "productId")
    
    merged_df = pd.merge(orders_df, inventory_df, on="primaryProductId", how="left", suffixes=("_order", "_inventory"))
    return merged_df

if __name__ == "__main__":
    # Define where the CSV files are located.
    orders_path = Path("data/raw/orders.csv")
    inventory_path = Path("data/raw/inventory.csv")
    
    # Load the CSV data using our ingestion function.
    orders_df = read_csv_file(orders_path)
    inventory_df = read_csv_file(inventory_path)
    
    # Merge the orders and inventory data on the simple product ID.
    merged_df = merge_orders_and_inventory(orders_df, inventory_df)
    
    # Print out the first few rows so we can check the merge worked as expected.
    print("Merged Data Preview:")
    print(merged_df.head())
