import pandas as pd

# Reading sample data with 200 rows
chunks = pd.read_csv("week2/day6/employees_sample.csv", chunksize=200)

# Slide 22: Chunk Processing for Large Files
total_salary = chunks["salary"].sum()
print(total_salary.dtype)
print("Total salary:", total_salary)