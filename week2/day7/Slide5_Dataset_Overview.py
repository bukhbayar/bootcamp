# Summary of dataset
print("Columns in dataset:", df.columns.tolist())
print("\nData types and non-null counts:")
print(df.info())

# Show count of missing values per column
print("\nMissing values per column:")
print(df.isnull().sum())

# Preview unique values for key features
print("\nUnique values for 'pclass':", df['Pclass'].unique())
print("Unique values for 'sex':", df['Sex'].unique())
