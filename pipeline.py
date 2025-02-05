# pipeline.py
import pandas as pd
from pathlib import Path
from src.ingestion import read_csv_file
from src.transform import merge_orders_and_inventory
from src.persistence import persist_to_sql
from src.reporting import run_reports
from src.validations import validate_order_record, validate_inventory_record

def validate_dataframe(df: pd.DataFrame, validate_func) -> pd.DataFrame:
    valid_records = []
    for idx, row in df.iterrows():
        validated = validate_func(row.to_dict())
        if validated:
            valid_records.append(validated)
    return pd.DataFrame(valid_records)

def run_pipeline():
    # Define file paths for raw data.
    orders_path = Path("data/raw/orders.csv")
    inventory_path = Path("data/raw/inventory.csv")
    
    # Step 1: Ingest Data
    print("Ingesting raw data...")
    orders_df = read_csv_file(orders_path)
    inventory_df = read_csv_file(inventory_path)

    # Step 2: Validate Orders Data
    print("Validating orders data...")
    validated_orders_df = validate_dataframe(orders_df, validate_order_record)
    
    # Step 3: Transform Data
    print("Transforming data...")
    # Use the validated orders for transformation
    merged_df = merge_orders_and_inventory(validated_orders_df, inventory_df)
    
    # Step 4: Persist Data (to SQLite and intermediate CSVs)
    print("Persisting data to database and CSV files...")
    persist_to_sql(orders_path, inventory_path)
    
    # Step 5: Reporting
    print("Running reports...")
    run_reports()

    print("Pipeline execution complete.")

if __name__ == "__main__":
    run_pipeline()
