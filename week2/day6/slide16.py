import pandas as pd

df = pd.read_csv("week2/day6/employees_sample.csv")

# Slide 16: Optimizing Memory
print('\n---- Before ----\n')
print("\nEach columns' memory:")
print(df.memory_usage(deep=True))
print("\nTotal Memory(MBs) :")
print(df.memory_usage(deep=True).sum() / 1e6)  # MBs


df["department"] = df["department"].astype("category")
df["city"] = df["city"].astype("category")

print('\n---- After ----\n')
print("Each columns' memory:")
print(df.memory_usage(deep=True))
print("\nTotal Memory(MBs) :")
print(df.memory_usage(deep=True).sum() / 1e6)  # MBs