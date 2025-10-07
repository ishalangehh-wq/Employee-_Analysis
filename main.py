import pandas as pd

# 1. Read CSV file
df = pd.read_csv("employee.csv")
print(df)

# 2. Check shape of DataFrame
print(df.shape)

# 3. Info about DataFrame
print(df.info())

# 4. Column names
print(df.columns)

# 5. Select specific columns
print(df[["Name", "Department"]])

# 6. Filter rows based on Experience > 3
print(df[df["Experience"] > 3])

# 7. Sort DataFrame by Salary in descending order
s = df.sort_values(by="Salary", ascending=False)
print(s)

# 8. Average Salary per Department
avg_salary = df.groupby("Department")["Salary"].mean()
print(avg_salary)

# 9. Total Experience per Department
total_exp = df.groupby("Department")["Experience"].sum()
print(total_exp)

# 10. Average Salary per Department for Active employees only
s_active = df[df["Status"] == "Active"].groupby("Department")["Salary"].mean()
print(s_active)

# 11. Pivot Table: count of employees per Department and Status
pivot_table = df.pivot_table(index="Department",
                             columns="Status",
                             values="Salary",
                             aggfunc="count",
                             fill_value=0)
print(pivot_table)

# 12. Salary statistics per Department: mean, max, sum
salary_status = df.groupby("Department")["Salary"].agg(["mean", "max", "sum"])
print(salary_status)

# 13. Add Bonus column: 10% of Salary
df["Bonus"] = df["Salary"] * 0.10
print(df)

# 14. Add Emp_status column based on Salary threshold
df["Emp_status"] = [
    "Active" if salary > 50000 else "Inactive" for salary in df["Salary"]
]
print(df[["Name", "Salary", "Emp_status"]])

# 15. Filter Inactive employees
print(df[df["Emp_status"] == "Inactive"])

# 16. Max Bonus per Department
max_bonus = df.groupby("Department")["Bonus"].max()
print(max_bonus)


# 17. Add performances column based on Salary
def performances(salary):
    if salary > 60000:
        return "High"
    elif 45000 <= salary <= 60000:
        return "Medium"
    else:
        return "Low"


df["performances"] = df["Salary"].apply(performances)
print(df[["Name", "performances", "Salary"]])
