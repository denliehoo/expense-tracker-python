import pandas as pd

# df = pd.read_csv("database/individual_data/testing.csv", index_col="Date" )
# print(df)
# print(df.shape)

# # list_val = list(df.columns.values)
# # list_val = df['Date'].tolist()
# # print(list_val)
# # print(df)


# # initial_amount = (df.iloc[2,1]) #have to convery the numpyin64 object to a float
# # print("initial amt",initial_amount)
# df.loc["2021-01-02","Books"] +=1000  #adds the amount to an exisiting value # if we use the column as a date, we can use the column name (e.g. the date as the val)
# in other cases, we use the index because the index is the col name. 

# print(df)




