# Import seaborn and prepare pairplot
import seaborn as sns
import matplotlib.pyplot as plt

# Drop NA values for selected features
selected_cols = ['Age', 'Fare', 'Pclass', 'Survived']
df_clean = df[selected_cols].dropna()

# Create pairplot
sns.pairplot(df_clean, hue='Survived')
plt.suptitle("Pairwise Relationships", y=1.02)
plt.show()
