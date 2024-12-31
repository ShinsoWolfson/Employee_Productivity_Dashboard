import pandas as pd
import sqlite3

# Load the dataset
file_path = '../data/employee_performance_.csv'
data = pd.read_csv(file_path)

# Clean column names
data.columns = data.columns.str.strip()

# Connect to SQLite database
db_path = '../data/employee_data.db'
conn = sqlite3.connect(db_path)

# Write data the database
data.to_sql('employee_performance', conn, if_exists='replace', index=False)
print("Data loaded into employee_performance table.")

# Close connection
conn.close()
