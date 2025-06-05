import pandas as pd

# Create a simple dataset using a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Daisy'],
    'Age': [25, 30, 35, 28],
    'Score': [85, 90, 95, 88]
}

# Convert it into a DataFrame
df = pd.DataFrame(data)

# Show the full table
print("📋 Full Data:")
print(df)

# Filter: Show people with Score > 88
print("\n🔍 People with Score > 88:")
print(df[df['Score'] > 88])

# Average score
average = df['Score'].mean()
print(f"\n📊 Average Score: {average}")
