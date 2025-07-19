import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv("job_dataset_cleaned.csv")

os.makedirs("static_graphs", exist_ok=True)

# Clean data
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
df["salary_cleaned"] = df["salary_range"].astype(str).str.extract(r"(\d+)").astype(float)
df["experience_cleaned"] = df["experience"].astype(str).str.extract(r"(\d+)").astype(float)

# Salary Distribution
plt.figure(figsize=(8,4))
sns.histplot(df["salary_cleaned"].dropna(), bins=30, kde=True)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.tight_layout()
plt.savefig("static_graphs/salary_distribution.png")
plt.close()

# Experience Boxplot
plt.figure(figsize=(8,4))
sns.boxplot(x=df["experience_cleaned"].dropna())
plt.title("Experience Boxplot")
plt.xlabel("Years of Experience")
plt.tight_layout()
plt.savefig("static_graphs/experience_boxplot.png")
plt.close()

# Top Companies
plt.figure(figsize=(8,4))
top_companies = df["company"].value_counts().head(10)
sns.barplot(y=top_companies.index, x=top_companies.values)
plt.title("Top Hiring Companies")
plt.tight_layout()
plt.savefig("static_graphs/top_companies.png")
plt.close()

# Roles
plt.figure(figsize=(8,4))
top_roles = df["role"].value_counts().head(10)
sns.barplot(y=top_roles.index, x=top_roles.values)
plt.title("Top Roles")
plt.tight_layout()
plt.savefig("static_graphs/top_roles.png")
plt.close()

# Work Type
plt.figure(figsize=(6, 4))
df["work_type"].value_counts().plot.pie(autopct="%1.1f%%")
plt.title("Work Type Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("static_graphs/work_type_distribution.png")
plt.close()
