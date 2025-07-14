import pandas as pd

# Slide 7: Checking Data Quality

df = pd.read_csv("week2/day6/employees_sample.csv")
print('''
      ---df.isnull().sum()---
      ''')
print(df.isnull().sum())

print('''
      ---df.duplicated().sum()---
      ''')
print(df.duplicated().sum())

print('''
      ---df["department"].unique()---
      ''')
print(df["department"].unique())

print('''
      ---df["gender"].value_counts()---
      ''')
print(df["gender"].value_counts())
