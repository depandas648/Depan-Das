import pandas as pd
import sqlite3

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [30, 22, 28],
    "City": ["New York", "Boston", "Chicago"]
}

# Create CSV
df = pd.DataFrame(data)
df.to_csv("sample.csv", index=False)

# Create Excel
df.to_excel("sample.xlsx", index=False, engine="openpyxl")

# Create SQLite DB
conn = sqlite3.connect("sample.db")
conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
conn.execute("DELETE FROM users")  # Clear previous data if any
conn.executemany(
    "INSERT INTO users (id, name, age) VALUES (?, ?, ?)",
    [(1, "Alice", 30), (2, "Bob", 25), (3, "Charlie", 28)],
)
conn.commit()
conn.close()

print("Sample files created successfully!")
