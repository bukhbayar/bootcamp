
# Slide 4: Loading Data
import pandas as pd
df = pd.read_csv("employees_sample.csv")
df.head()

df.tail()
df.sample(5)

# Slide 5: Basic Inspection
df.info()
df.describe()

df.columns
df.dtypes

# Slide 6: Checking Data Quality
df.isnull().sum()
df.duplicated().sum()

df["department"].unique()
df["gender"].value_counts()

# Slide 7: Filtering Data
df[df["age"] > 60]
df[df["department"] == "Sales"]

# Slide 8: Applying Multiple Conditions
df[(df["age"] > 40) & (df["department"] == "Finance")]
df[(df["salary"] > 100000) | (df["city"] == "Melbourne")]

# Slide 9: Cleaning Text Data
df["email"] = df["first_name"].str.lower() + "." + df["last_name"].str.lower() + "@company.com"
df["city"] = df["city"].str.strip().str.title()

# Slide 10: Working with Dates
df["hire_date"] = pd.to_datetime(df["hire_date"])
df["hire_year"] = df["hire_date"].dt.year

df["tenure"] = 2025 - df["hire_year"]
df["hire_month"] = df["hire_date"].dt.month

# Slide 11: Categorizing Data
bins = [0, 60000, 90000, 150000]
labels = ["Low", "Mid", "High"]
df["salary_band"] = pd.cut(df["salary"], bins=bins, labels=labels)

df["salary_band"].value_counts()
df["salary_band"] = df["salary_band"].astype("category")

# Slide 12: Grouping and Aggregation
df.groupby("department")["salary"].mean()
df.groupby("department").agg({"salary": ["mean", "max", "min"]})

# Slide 13: Filtering After Grouping
dept_stats = df.groupby("department").agg(avg_salary=("salary", "mean"), headcount=("employee_id", "count"))
dept_stats[dept_stats["headcount"] > 100]

dept_stats.reset_index(inplace=True)
dept_stats.sort_values("avg_salary", ascending=False)

# Slide 14: Creating Pivot Tables
pd.pivot_table(df, values="employee_id", index="salary_band", columns="gender", aggfunc="count")
pd.pivot_table(df, values="salary", index="department", columns="gender", aggfunc="mean")

# Slide 15: Optimizing Memory
df["department"] = df["department"].astype("category")
df["city"] = df["city"].astype("category")

df.memory_usage(deep=True)
df.memory_usage(deep=True).sum() / 1e6  # MBs

# Slide 16: Identifying Non-Matching Records
df_reviews = df.sample(600)[["employee_id", "performance_score"]]
anti_join = df.merge(df_reviews, on="employee_id", how="left", indicator=True)

anti_join = anti_join[anti_join["_merge"] == "left_only"]
anti_join[["employee_id", "department"]].head()

# Slide 17: Merging Datasets
budgets = pd.DataFrame({"department": ["IT", "Sales"], "budget": [2000000, 3000000]})
df = df.merge(budgets, on="department", how="left")

df["budget"].fillna(0, inplace=True)
df[df["budget"] == 0].head()

# Slide 18: Data Validation
assert df["age"].between(18, 65).all(), "Age out of range"
assert df["salary"].notnull().all(), "Missing salary"

assert df["department"].isin(["HR", "IT", "Sales", "Marketing", "Finance", "Operations"]).all()
assert df["tenure"].ge(0).all()

# Slide 19: Quick Visual Summaries
df["salary"].hist(bins=30)
df["department"].value_counts().plot(kind="bar")

# Slide 20: Scatter Plot for Insight
df.plot.scatter(x="tenure", y="salary", alpha=0.6)
df.plot.scatter(x="performance_score", y="salary", c="age", colormap="viridis")

# Slide 21: Chunk Processing for Large Files
chunks = pd.read_csv("employees_sample.csv", chunksize=200)
total_salary = 0
for chunk in chunks:
    total_salary += chunk["salary"].sum()

print("Total salary:", total_salary)

# Slide 22: Profiling Performance
%timeit df["salary"].mean()
%timeit df.groupby("department")["salary"].mean()

# Slide 23: Logging
import logging, sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.info("Data loaded with %d rows", len(df))

# Slide 24: Validating Data Types
from pandas.api.types import is_numeric_dtype
if is_numeric_dtype(df["performance_score"]):
    df["performance_score"].fillna(df["performance_score"].mean(), inplace=True)

if not is_numeric_dtype(df["department"]):
    print("Department is not numeric – expected.")

# Slide 25: List and Dictionary Tools
email_list = [f"{r.first_name.lower()}.{r.last_name.lower()}@test.com" for _, r in df.iterrows()]
dept_map = {r.employee_id: r.department for _, r in df.iterrows()}
