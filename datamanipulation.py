import pandas as pd
import numpy as np
import sqlite3  # Built-in database

# === Load from CSV ===
csv_df = pd.read_csv("sample.csv")  # Replace with your CSV file path
print("\n📄 CSV Data:\n", csv_df.head())

# === Load from Excel ===
excel_df = pd.read_excel("sample.xlsx", engine="openpyxl")  # Requires openpyxl
print("\n Excel Data:\n", excel_df.head())

# === Load from SQLite Database ===
conn = sqlite3.connect("sample.db")  # Your SQLite DB file
sql_df = pd.read_sql_query("SELECT * FROM users", conn)
print("\n SQL Data:\n", sql_df.head())

# === Data Cleaning Example ===
# Drop rows with missing values
cleaned_df = csv_df.dropna()

# Rename columns
cleaned_df.rename(columns={"old_name": "new_name"}, inplace=True)

# Filter rows
filtered_df = cleaned_df[cleaned_df["Age"] > 25]

# === Add a calculated column ===
filtered_df["Age*2"] = filtered_df["Age"] * 2

# === Summary statistics ===
print("\n Summary Stats:\n", filtered_df.describe())

# === Export back to CSV ===
filtered_df.to_csv("output.csv", index=False)

# === Close SQL connection ===
conn.close()
