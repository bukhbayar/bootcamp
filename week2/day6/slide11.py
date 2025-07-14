import pandas as pd

# Slide 11: Working with Dates

df = pd.read_csv("week2/day6/employees_sample.csv")
print('''---
      Check hire_date, hire_year, tenure, hire_month columns
      ---''')

df["hire_date"] = pd.to_datetime(df["hire_date"])
df["hire_year"] = df["hire_date"].dt.year

df["tenure"] = 2025 - df["hire_year"]
df["hire_month"] = df["hire_date"].dt.month

print(df.head(5))
