import pandas as pd

df = pd.read_csv("week2/day6/employees_sample.csv")

# Slide 20: Quick Visual Summaries
df["salary"].hist(bins=30)
df["department"].value_counts().plot(kind="bar")
