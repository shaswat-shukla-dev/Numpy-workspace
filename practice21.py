import pandas as pd

df = pd.read_csv('automobile_data.csv')   

print(df.head())


expensive = df.loc[df['price'].idxmax()]

print("\nMost Expensive Automobile:")
print(expensive[['company', 'price']])
name_toyota = df.loc[df['company'] == 'toyota']

print("\nAll cars with Toyota:")
print(name_toyota)
print(df.count())
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df = df.dropna(subset=['price'])

cheapest_cars = df.loc[df.groupby('company')['price'].idxmin()]

print("Cheapest car of each company:\n")
print(cheapest_cars[['company', 'price']])