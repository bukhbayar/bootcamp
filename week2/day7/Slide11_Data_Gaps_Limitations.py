# Missing value summary
print("Missing values per column:")
print(df.isnull().sum())

# Percentage missing
missing_percentage = df.isnull().mean().round(4) * 100
print("\nPercentage missing:")
print(missing_percentage)

# Decision hint
print("\nRecommendation:")
print("- 'cabin' has too many missing values → consider dropping it.")
print("- 'embarked' and 'age' → consider filling or imputing.")


#test
