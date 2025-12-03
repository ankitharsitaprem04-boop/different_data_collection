import pandas as pd

df = pd.read_excel("data.xlsx", sheet_name=0)
print(df.head())
