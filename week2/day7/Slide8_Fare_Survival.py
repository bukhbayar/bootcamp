# Boxplot: Fare vs Survival
sns.boxplot(data=df, x='Survived', y='Fare')
plt.title("Fare Distribution by Survival")
plt.xlabel("Survived")
plt.ylabel("Fare")
plt.show()

# Correlation between fare and survival
fare_survival_corr = df[['Fare', 'Survived']].corr().iloc[0,1]
print("Correlation between Fare and Survival:", fare_survival_corr)
