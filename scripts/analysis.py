import sqlite3
import pandas as pd

# Connect to SQLite database
db_path = '../data/employee_data.db'
conn = sqlite3.connect(db_path)

# Query 1: Total Tasks Completed by Department
query_department_tasks = """
SELECT Department, SUM(Projects_Handled) AS TotalTasks
FROM employee_performance
GROUP BY Department;
"""
department_tasks = pd.read_sql_query(query_department_tasks, conn)

# Query 2: Average Productivity per Employee
query_employee_productivity = """
SELECT Employee_ID, AVG(Projects_Handled * 1.0 / Work_Hours_Per_Week) AS Productivity
FROM employee_performance
GROUP BY Employee_ID;
"""
employee_productivity = pd.read_sql_query(query_employee_productivity, conn)

# Query 3: Overall Department Productivity
query_department_productivity = """
SELECT Department, AVG(Projects_Handled * 1.0 / Work_Hours_Per_Week) as AvgProductivity
FROM employee_performance
GROUP BY Department;
"""
department_productivity = pd.read_sql_query(query_department_productivity, conn)

# Close connection
conn.close()

# Save results to CSV for visualization
department_tasks.to_csv('../data/department_tasks.csv', index=False)
employee_productivity.to_csv('../data/employee_productivity.csv', index=False)
department_productivity.to_csv('../data/department_productivity.csv', index=False)
print("Analysis results saved as CSV files.")
