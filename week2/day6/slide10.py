import pandas as pd

# Slide 10: Cleaning Text Data

df = pd.read_csv("week2/day6/employees_sample.csv")
print('''
      ---df["email"] = df["first_name"].str.lower() + "." + df["last_name"].str.lower() + "@company.com"---
      ''')
df["email"] = df["first_name"].str.lower() + "." + df["last_name"].str.lower() + "@company.com"
print(df.head())

print('''
      ---df["city"] = df["city"].str.strip().str.title()---
      ''')
df["city"] = df["city"].str.strip().str.title()
print(df.head())
