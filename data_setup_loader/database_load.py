import sqlite3

conn = sqlite3.connect("northwind.db")

cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

for t in tables:
    print(t)


import pandas as pd
table_name = "customers" 
df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)

print(df.info())