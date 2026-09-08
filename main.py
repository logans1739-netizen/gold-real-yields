import pandas as pd
df = pd.read_csv('https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFII10')
df.head(5)
print(df.columns)
print(df.dtypes)
df['observation_date'] = pd.to_datetime(df['observation_date'])
print(df.dtypes)

