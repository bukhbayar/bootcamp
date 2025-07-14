import pandas as pd
from pandas.api.types import is_numeric_dtype

df = pd.read_csv("week2/day6/employees_sample.csv")

# Slide 25: Validating Data Types

if is_numeric_dtype(df["performance_score"]):
    df.fillna({"performance_score": df["performance_score"].mean()}, inplace=True)

if not is_numeric_dtype(df["department"]):
    print("Department is not numeric - expected.")
