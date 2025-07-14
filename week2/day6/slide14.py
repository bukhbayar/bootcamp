import pandas as pd

df = pd.read_csv("week2/day6/employees_sample.csv")

# Slide 14: Filtering After Grouping


print('''
      ---Check avg_salary, headcount columns and group by---
      ''')
dept_stats = df.groupby("department").agg(avg_salary=("salary", "mean"), headcount=("employee_id", "count"))
dept_stats[dept_stats["headcount"] > 100]

print(dept_stats.head())