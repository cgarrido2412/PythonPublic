#combine spreadsheets side by side, for example, combine store circuit spreadsheets
data1 = pd.read_excel('E:\Savers\Spreadsheets\pandasDataframe1.xlsx') #old sheet from May
data2 = pd.read_excel('E:\Savers\Spreadsheets\dataframe2.xlsx') #newer sheet from september
df_merge_col = pd.merge(data2, data1, on='Name') #This put the new file first, and the old sheet second
df_merge_col.to_excel('E:\Savers\Spreadsheets\checkStoreCircuits.xlsx') #saves as a new file
