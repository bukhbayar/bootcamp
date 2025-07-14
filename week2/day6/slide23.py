import pandas as pd
import time

df = pd.read_csv("week2/day6/employees_sample.csv")

# Slide 23: Profiling Performance
start = time.time()
df["salary"].mean()
end = time.time()
print("Execution time:", end - start, "seconds")

# %timeit would work on Jupyter Notebook only
# %timeit df.groupby("department")["salary"].mean()