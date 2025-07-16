import pandas as pd
import json

# Load local JSON file
with open("employees.json") as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data["employees"])

# Show the data
print("Original DataFrame:")
print(df)

# Filter employees older than 30
older_than_30 = df[df["age"] > 30]
print("\nEmployees older than 30:")
print(older_than_30)

# Apply a function to create a new column
def seniority(age):
    return "Senior" if age > 30 else "Junior"

df["seniority"] = df["age"].apply(seniority)

# Group by department
grouped = df.groupby("department")["age"].mean()
print("\nAverage age by department:")
print(grouped)
