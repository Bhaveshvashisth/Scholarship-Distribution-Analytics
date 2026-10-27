"""
Scholarship Distribution Analytics
Course: Foundations of Data Science (CCSDS0301)
Author: Bhavesh Vashisth

Steps: load raw data -> clean -> transform -> aggregate -> visualise -> export.
Run:  python analysis.py
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

RAW_FILE = "data/raw_scholarship_data.csv"
CLEAN_FILE = "data/cleaned_scholarship_data.csv"
OUT_DIR = "outputs"
os.makedirs(OUT_DIR, exist_ok=True)

# ---------------------------------------------------------------- 1. Load
raw = pd.read_csv(RAW_FILE)
print("Raw records:", len(raw))

# --------------------------------------------------------------- 2. Clean
df = raw.copy()

# remove extra spaces from text columns
for col in ["Student_ID", "Department", "Category", "Status"]:
    df[col] = df[col].astype(str).str.strip()

# standardise department names (CSE, C.S.E., Computer Science -> CSE)
dept_map = {
    "cse": "CSE", "c.s.e.": "CSE", "computer science": "CSE",
    "ece": "ECE", "e.c.e.": "ECE", "electronics": "ECE",
    "me": "ME", "m.e.": "ME", "mechanical": "ME",
    "civil": "Civil",
}
df["Department"] = df["Department"].str.lower().map(dept_map)

# standardise category names
df["Category"] = df["Category"].str.upper().replace({"GENERAL": "General"})

# missing values and duplicates
print("Missing values:\n", df.isnull().sum(), sep="")
df = df.dropna()
before = len(df)
df = df.drop_duplicates()
print("Duplicate records removed:", before - len(df))

df.to_csv(CLEAN_FILE, index=False)
print("Clean records:", len(df))

# ----------------------------------------------------- 3. Transform
# group family income into bands (used for income-group analysis)
bins = [0, 200000, 300000, float("inf")]
labels = ["Below 2 lakh", "2 to 3 lakh", "Above 3 lakh"]
df["Income_Group"] = pd.cut(df["Family_Income"], bins=bins, labels=labels, right=False)

# min-max normalisation of scholarship amount
amt = df["Scholarship_Amount"]
df["Amount_Normalized"] = (amt - amt.min()) / (amt.max() - amt.min())

# ----------------------------------------------------- 4. Aggregate
total = df["Scholarship_Amount"].sum()
average = df["Scholarship_Amount"].mean()
print(f"\nTotal scholarship: Rs. {total:,.0f}")
print(f"Average scholarship: Rs. {average:,.0f}")

def summary(column):
    t = df.groupby(column, observed=True).agg(
        Students=("Student_ID", "count"),
        Total=("Scholarship_Amount", "sum"),
        Average=("Scholarship_Amount", "mean"),
    )
    t["Share_%"] = (t["Total"] / total * 100).round(1)
    return t.sort_values("Total", ascending=False)

dept = summary("Department")
cat = summary("Category")
income = summary("Income_Group")
print("\nDepartment-wise:\n", dept, sep="")
print("\nCategory-wise:\n", cat, sep="")
print("\nIncome group-wise:\n", income, sep="")

# ------------------------------------------------------ 5. Visualise
fig, ax = plt.subplots(1, 2, figsize=(9, 3.8))
ax[0].bar(dept.index, dept["Total"] / 1000, color="#1F4E79")
ax[0].set_title("Scholarship amount by department")
ax[0].set_ylabel("Amount (Rs. thousand)")
ax[1].bar(dept.index, dept["Students"], color="#2E75B6")
ax[1].set_title("Scholarship recipients by department")
ax[1].set_ylabel("Number of students")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/department_charts.png", dpi=200)
plt.close()

fig, ax = plt.subplots(1, 2, figsize=(9, 3.8))
ax[0].pie(cat["Students"], labels=cat.index, autopct="%1.1f%%", startangle=90)
ax[0].set_title("Students by category")
ax[1].bar(cat.index, cat["Average"] / 1000, color="#2E75B6")
ax[1].axhline(average / 1000, color="#C55A11", linestyle="--")
ax[1].set_title("Average scholarship per student")
ax[1].set_ylabel("Amount (Rs. thousand)")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/category_charts.png", dpi=200)
plt.close()

# --------------------------------------------------------- 6. Export
with pd.ExcelWriter(f"{OUT_DIR}/scholarship_analysis.xlsx") as xw:
    raw.to_excel(xw, sheet_name="Raw_Data", index=False)
    df.to_excel(xw, sheet_name="Cleaned_Data", index=False)
    dept.to_excel(xw, sheet_name="Department_Summary")
    cat.to_excel(xw, sheet_name="Category_Summary")
    income.to_excel(xw, sheet_name="Income_Summary")
print("\nCharts and Excel workbook saved in the outputs folder.")
