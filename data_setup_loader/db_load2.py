import sqlite3

conn = sqlite3.connect("northwind.db")
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

tables = cursor.fetchall()

for t in tables:
    print(t[0])

table_name = "customers" 

import pandas as pd

df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)

print(df.info())

#mysql, #posgresql #mongodb