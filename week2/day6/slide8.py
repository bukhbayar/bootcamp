import pandas as pd

# Slide 8: Filtering Data

df = pd.read_csv("week2/day6/employees_sample.csv")

print('''
      ---df[df["age"] > 60]---
      ''')
df[df["age"] > 60]

print('''
      ---df[df["department"] == "Sales"]---
      ''')
print(df[df["department"] == "Sales"])