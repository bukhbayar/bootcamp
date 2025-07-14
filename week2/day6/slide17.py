import pandas as pd

df = pd.read_csv("week2/day6/employees_sample.csv")

# Slide 17: Identifying Non-Matching Records
print('''
      --- Sample data with 600 records ---
      ''')
df_reviews = df.sample(600)[["employee_id", "performance_score"]]
print(df_reviews.head(10))

print('''
      --- Merged record, Check "_merge" column ---
      ''')
anti_join = df.merge(df_reviews, on="employee_id", how="left", indicator=True)
print(anti_join.head(10))

print('''
      --- Filtered by "left_only" means, it will get data that did not find a match from df_review table ---
      ''')
anti_join = anti_join[anti_join["_merge"] == "left_only"]
print(anti_join[["employee_id", "department"]].head())