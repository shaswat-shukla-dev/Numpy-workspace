import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["Delhi", "Mumbai", "Bangalore"]
}

df = pd.DataFrame(data)

df.to_csv("automobile_data.csv", index=False)
df = pd.read_csv("automobile_data.csv")

print(df)