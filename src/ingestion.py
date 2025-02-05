# src/ingestion.py

from pathlib import Path
import pandas as pd
from typing import Tuple

def read_csv_file(file_path: Path) -> pd.DataFrame:
    """Reads a CSV file and returns a DataFrame."""
    return pd.read_csv(file_path)

def ingest_data(orders_file: Path, inventory_file: Path) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Reads the orders and inventory CSV files.
    Tuple containing the orders DataFrame and the inventory DataFrame.
    """
    orders_df = read_csv_file(orders_file)
    inventory_df = read_csv_file(inventory_file)
    return orders_df, inventory_df

if __name__ == "__main__":
    # Adjust the path if needed
    orders_path = Path("data/raw/orders.csv")
    inventory_path = Path("data/raw/inventory.csv")
    orders, inventory = ingest_data(orders_path, inventory_path)
    
    print("Orders Data Preview:")
    print(orders.head())
    
    print("\nInventory Data Preview:")
    print(inventory.head())
