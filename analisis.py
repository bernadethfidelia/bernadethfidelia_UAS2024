import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib_venn import venn2

# Membuat DataFrame dari data
data = {
    'Employee_ID': [1, 2, 3, 4, 5, 6, 7, 8],
    'Department': ['HR', 'IT', 'Sales', 'Marketing', 'IT', 'HR', 'Sales', 'Marketing'],
    'Salary': [5000, 7000, 6000, 6500, 7200, 4800, 5800, 6300],
    'Years_of_Experience': [3, 5, 4, 6, 8, 2, 3, 4]
}
df = pd.DataFrame(data)

# Scatterplot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Years_of_Experience', y='Salary', hue='Department', data=df, s=100)
plt.title('Scatterplot of Salary vs. Years of Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.legend(title='Department')
plt.show()

# Grafik Garis
plt.figure(figsize=(10, 6))
for department in df['Department'].unique():
    subset = df[df['Department'] == department]
    plt.plot(subset['Years_of_Experience'], subset['Salary'], marker='o', label=department)
plt.title('Line Plot of Salary vs. Years of Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.legend(title='Department')
plt.show()

# Grafik Batang
plt.figure(figsize=(10, 6))
sns.barplot(x='Department', y='Salary', data=df)
plt.title('Bar Plot of Average Salary by Department')
plt.xlabel('Department')
plt.ylabel('Average Salary')
plt.show()

# Grafik Titik
plt.figure(figsize=(10, 6))
sns.stripplot(x='Department', y='Salary', data=df, jitter=True)
plt.title('Dot Plot of Salary by Department')
plt.xlabel('Department')
plt.ylabel('Salary')
plt.show()

# Diagram Venn (contoh kondisi: IT vs. Sales, berdasarkan gaji lebih dari 6000)
it_high_salary = set(df[(df['Department'] == 'IT') & (df['Salary'] > 6000)]['Employee_ID'])
sales_high_salary = set(df[(df['Department'] == 'Sales') & (df['Salary'] > 6000)]['Employee_ID'])

plt.figure(figsize=(8, 6))
venn2([it_high_salary, sales_high_salary], ('IT > 6000', 'Sales > 6000'))
plt.title('Venn Diagram of High Salary Employees in IT and Sales')
plt.show()
