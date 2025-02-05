import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path
from src.transform import merge_orders_and_inventory  
from src.ingestion import read_csv_file 

def persist_to_sql(orders_path: Path, inventory_path: Path, table_name: str = "merged_data", db_url: str = "sqlite:///data/processed/processed.db"):
    # Read the data
    orders_df = read_csv_file(orders_path)
    inventory_df = read_csv_file(inventory_path)
    
    # Merge (transform) the data
    merged_df = merge_orders_and_inventory(orders_df, inventory_df)
    
    # Create a database engine and save the DataFrame to SQL
    engine = create_engine(db_url)
    merged_df.to_sql(table_name, con=engine, if_exists="replace", index=False)
    print(f"Merged data persisted to table '{table_name}' in database '{db_url}'.")

if __name__ == "__main__":
    orders_path = Path("data/raw/orders.csv")
    inventory_path = Path("data/raw/inventory.csv")
    persist_to_sql(orders_path, inventory_path)
