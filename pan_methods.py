import pandas as pd

data = {
    'Name': ['Virat', 'Rohit', 'Dhoni'],
    'Team': ['RCB', 'MI', 'CSK'],
    'Runs': [5400, 9200, 11000]
}

df = pd.DataFrame(data)

print("Cricket Players DataFrame:\n", df)

print("\nNames:\n", df['Name'])


print("\nStatistics:\n", df.describe())

df['Matches'] = [200, 240, 350]
print("\nAfter adding Matches column:\n", df)

head =df.head()
print(head)
print(df.info())
print(df.iloc[1])
