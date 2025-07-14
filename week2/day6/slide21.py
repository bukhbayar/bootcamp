import pandas as pd

df = pd.read_csv("week2/day6/employees_sample.csv")

# Slide 21: Scatter Plot for Insight
df.plot.scatter(x="tenure", y="salary", alpha=0.6)
df.plot.scatter(x="performance_score", y="salary", c="age", colormap="viridis")
