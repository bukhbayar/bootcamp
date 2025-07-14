import pandas as pd

df = pd.read_csv("week2/day6/employees_sample.csv")

# Slide 13: Grouping and Aggregation

print('''
      ---df.groupby("department")["salary"].mean()---
      ''')

print(df.groupby("department")["salary"].mean())

print('''
      ---df.groupby("department").agg({"salary": ["mean", "max", "min"]})---
      ''')
print(df.groupby("department").agg({"salary": ["mean", "max", "min"]}))
