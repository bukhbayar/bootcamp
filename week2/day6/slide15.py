import pandas as pd

df = pd.read_csv("week2/day6/employees_sample.csv")

# Slide 15: Creating Pivot Tables

bins = [0, 60000, 90000, 150000]
labels = ["Low", "Mid", "High"]
df["salary_band"] = pd.cut(df["salary"], bins=bins, labels=labels)

df["salary_band"].value_counts()
df["salary_band"] = df["salary_band"].astype("category")

print('''
      ---Check salary_band in row, gender in column and Aggregate function---
      ''')

pt1 = pd.pivot_table(df, values="employee_id", index="salary_band", columns="gender", aggfunc="count")
print(pt1.head())

print('''
      ---Check department in row, gender in gender and Aggregate function---
      ''')
pt2 = pd.pivot_table(df, values="salary", index="department", columns="gender", aggfunc="mean")
print(pt2.head())