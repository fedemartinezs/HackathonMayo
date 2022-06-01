import pandas as pd
df = pd.read_csv('data.txt')
dfj= df.iloc[7:10]
print(dfj)