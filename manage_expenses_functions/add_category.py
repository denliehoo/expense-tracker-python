def add_category(username,expense_data,new_cat):
    total_rows=expense_data.shape[0]
    new_column_data = []
    for i in range(total_rows):
        new_column_data.append(0)
    expense_data[new_cat] = new_column_data
    expense_data.to_csv("database/individual_data/"+username+".csv",index=False) #saves to the csv
    return 