# Survival by gender
survival_by_gender = df.groupby('Sex')['Survived'].mean()
print("Survival Rate by Gender:\n", survival_by_gender)

# Survival by class
survival_by_class = df.groupby('Pclass')['Survived'].mean()
print("\nSurvival Rate by Class:\n", survival_by_class)

# Survival by age group (minors vs adults)
df['is_minor'] = df['age'] < 18
survival_by_age_group = df.groupby('is_minor')['Survived'].mean()
print("\nSurvival Rate by Age Group (Minors vs Adults):\n", survival_by_age_group)
