import pandas as pd
df = pd.read_excel('every_other_lab.xlsx')
print(df)
df1 = df[df.index % 2 != 0] # Excludes every 2nd row starting from 0
print(df1)
#df1.to_excel('proof.xls', 'a+')
