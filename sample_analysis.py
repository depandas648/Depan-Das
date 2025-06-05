import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create sample data and save it to Excel
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 22],
    'Score': [85, 90, 95, 88, 92]
}
df = pd.DataFrame(data)
df.to_excel('sample_data.xlsx', index=False)

# Read the Excel file back
df = pd.read_excel('sample_data.xlsx')

# Show basic statistics
print("Basic statistics:")
print(df.describe())

# Plot Age vs. Score
sns.scatterplot(data=df, x='Age', y='Score')
plt.title('Age vs. Score')
plt.show()
