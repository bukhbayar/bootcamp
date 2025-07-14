import pandas as pd

# Slide 9: Applying Multiple Conditions

df = pd.read_csv("week2/day6/employees_sample.csv")

print('''
      ---df[(df["age"] > 40) & (df["department"] == "Finance")]---
      ''')
print(df[(df["age"] > 40) & (df["department"] == "Finance")])
print('''
      ---df[(df["salary"] > 100000) | (df["city"] == "Melbourne")]---
      ''')
print(df[(df["salary"] > 100000) | (df["city"] == "Melbourne")])