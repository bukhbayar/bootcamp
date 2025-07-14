import pandas as pd

df = pd.read_csv("week2/day6/employees_sample.csv")

df["email"] = df["first_name"].str.lower() + "." + df["last_name"].str.lower() + "@company.com"
df["city"] = df["city"].str.strip().str.title()

df["hire_date"] = pd.to_datetime(df["hire_date"])
df["hire_year"] = df["hire_date"].dt.year

df["tenure"] = 2025 - df["hire_year"]
df["hire_month"] = df["hire_date"].dt.month


# Slide 19: Data Validation
print('''
      --- if age field of all data is between 18 and 20, it wont return any message
      --- if not, it woll throw error message. e.g "Age out of range"
      ''')
assert df["age"].between(18, 20).all(), "Age out of range"
assert df["salary"].notnull().all(), "Missing salary"

assert df["department"].isin(["HR", "IT", "Sales", "Marketing", "Finance", "Operations"]).all()
assert df["tenure"].ge(0).all()