import pandas as pd

df = pd.read_csv("week2/day6/employees_sample.csv")

# Slide 18: Merging Datasets
budgets = pd.DataFrame({"department": ["IT", "Sales"], "budget": [2000000, 3000000]})
df = df.merge(budgets, on="department", how="left")

print('''
      --- fillna will replace NaN (NULL) values with 0 ---
      --- NaN (NULL) values will there because left join and if some rows did not match ---
      ''')
print(df.head(10))
df["budget"].fillna(0, inplace=True) # inplace=True will replace value in original dataframe
print(df.head(10))

print('''
      --- filtering budged == 0 which will include all those not matched records ---
      ''')
print(df[df["budget"] == 0].head())