
# Slide 5: Loading Data

import pandas as pd

df = pd.read_csv("week2/day6/employees_sample.csv")
print('''
      ---df.head()---
      ''')
print(df.head())

print('''
      ---df.tail()---
      ''')
print(df.tail())

print('''
      ---df.sample(5)---
      ''')
print(df.sample(5))
