import seaborn as sns
import matplotlib.pyplot as plt

# Gender distribution
sns.countplot(data=df, x='Sex')
plt.title("Passenger Gender Distribution")
plt.show()

# Age distribution
sns.histplot(df['Age'].dropna(), bins=30, kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.show()

# Class distribution
sns.countplot(data=df, x='Pclass')
plt.title("Passenger Class Distribution")
plt.show()
