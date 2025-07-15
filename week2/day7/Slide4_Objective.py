# Load necessary libraries
import pandas as pd

# Load Titanic dataset
df = pd.read_csv("./work/titanic.csv")

# Display dataset shape and first few rows
print("Dataset shape:", df.shape)
df.head()
