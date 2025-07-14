
# Slide 6: Basic Inspection

import pandas as pd

df = pd.read_csv("week2/day6/employees_sample.csv")
print('''
      --df.info()---
      ''')
print(df.info())

print('''
      ---df.describe()---
      ''')
print(df.describe())

print('''
      ---df.columns---
      ''')
print(df.columns)

print('''
      ---df.dtypes---
      ''')
print(df.dtypes)
