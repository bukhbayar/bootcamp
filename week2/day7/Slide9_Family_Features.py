# Analyze siblings/spouses aboard
sns.countplot(data=df, x='SibSp', hue='Survived')
plt.title("Survival by Number of Siblings/Spouses Aboard")
plt.show()

# Analyze parents/children aboard
sns.countplot(data=df, x='Parch', hue='Survived')
plt.title("Survival by Number of Parents/Children Aboard")
plt.show()
