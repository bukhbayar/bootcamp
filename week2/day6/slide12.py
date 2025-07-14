import pandas as pd

df = pd.read_csv("week2/day6/employees_sample.csv")

# Slide 12: Categorizing Data

bins = [0, 60000, 90000, 150000]
labels = ["Low", "Mid", "High"]
df["salary_band"] = pd.cut(df["salary"], bins=bins, labels=labels)

print('''
      ---df["salary_band"].value_counts()---
      ''')
print(df["salary_band"].value_counts())

print('''
      ---Check salary_band column---
      ''')
print(df.head(5))


# "category" data type and its differences
print('''
      Note* if data type is object, it will have high memory usage
      Before:
      ''')
print(df["department"].dtype)
df["department"] = df["department"].astype("category")
print('''
      Note* if data type is category, it will have low memory usage
      After:
      ''')
print(df["department"].dtype)