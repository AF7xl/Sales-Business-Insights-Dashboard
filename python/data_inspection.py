import pandas as pd

df=pd.read_csv("../data/superstore.csv",encoding="latin1")
print("\n== Shape ==")
print(df.shape)

print("\n== Columns ==")
print(df.columns)

print("\n== info ==")
print(df.info())

print("\n == head ==")
print(df.head())

print("\n == missing values ==")
print(df.isnull().sum())