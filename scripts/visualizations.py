import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load analysis results
department_tasks = pd.read_csv('../data/department_tasks.csv')
employee_prod = pd.read_csv('../data/employee_productivity.csv')
department_prod = pd.read_csv('../data/department_productivity.csv')
sampled_data = employee_prod.sample(n=50, random_state=42)

# Plot 1: Total Tasks Completed by Department
plt.figure(figsize=(10, 6))
sns.barplot(data=department_tasks, x='Department', y='TotalTasks', hue='Department', palette='viridis', legend=False)
plt.title('Total Tasks Completed by Department')
plt.xlabel('Department')
plt.ylabel('Total Tasks')
plt.tight_layout()
plt.savefig('../dashboards/department_tasks.png')
plt.show()

# Plot 2: Average Productivity per Employee (Sample Size for Easier Interpretation)
plt.figure(figsize=(12, 6))
sns.barplot(data=sampled_data, x='Employee_ID', y='Productivity', hue='Employee_ID', palette='mako', legend=False)
plt.title('Productivity of Sampled Employees')
plt.xlabel('Employee ID')
plt.ylabel('Tasks per Hour')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('../dashboards/employee_productivity.png')
plt.show()

# Plot 3: Average Productivity by Department
plt.figure(figsize=(10, 6))
sns.barplot(data=department_prod, x='Department', y='AvgProductivity', hue='Department', palette='cool', legend=False)
plt.title('Average Productivity by Department')
plt.xlabel('Department')
plt.ylabel('Avg Tasks per Hour')
plt.tight_layout()
plt.savefig('../dashboards/department_productivity.png')
plt.show()
