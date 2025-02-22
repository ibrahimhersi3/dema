# src/reporting.py

from sqlalchemy import create_engine, text

def run_reports(db_url: str = "sqlite:///data/processed/processed.db"):
    # Create a database engine
    engine = create_engine(db_url)
    
    with engine.connect() as connection:
        # Report 1: Count of orders per primary product ID
        query1 = text("""
            SELECT primaryProductId, COUNT(*) AS order_count
            FROM merged_data
            GROUP BY primaryProductId
        """)
        print("Order Count per Primary Product ID:")
        for row in connection.execute(query1):
            print(row)
        
        print("\n" + "="*40 + "\n")
        
        # Report 2: Total sales amount per product
        query2 = text("""
            SELECT primaryProductId, SUM(amount) AS total_sales
            FROM merged_data
            GROUP BY primaryProductId
        """)
        print("Total Sales per Primary Product ID:")
        for row in connection.execute(query2):
            print(row)
        
        print("\n" + "="*40 + "\n")

        # Report 3: Total orders and average order amount per category
        query3 = text("""
            SELECT category, COUNT(*) AS total_orders, AVG(amount) AS average_order_amount
            FROM merged_data
            GROUP BY category;
        """)
        print("Orders and Average Order Amount per Category:")
        for row in connection.execute(query3):
            print(row)
        
       

if __name__ == "__main__":
    run_reports()
