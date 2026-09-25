import duckdb
import os

csv_path = 'data/cleaned/customer_churn_cleaned.csv'
db_path = 'data/churn_database.duckdb'

print(f"Creating DuckDB database at {db_path}...")

con = duckdb.connect(db_path)

# table from csv 
print("Loading data into 'customers' table...")
con.execute(f"""
    CREATE TABLE customers AS 
    SELECT * FROM read_csv_auto('{csv_path}')
""")

print("Data loaded successfully!")

# count verify
count = con.execute("SELECT COUNT(*) FROM customers").fetchone()[0]
print(f"Total rows inserted: {count}")

con.close()
