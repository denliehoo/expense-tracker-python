import pandas as pd 

def check_existing_date_and_category(input_category,input_date,username):
    expense_data=pd.read_csv("database/individual_data/"+username+".csv")
    category_values = list(expense_data.columns.values)[1:]
    date_values = expense_data["Date"].tolist()
    if input_date not in date_values or input_category not in category_values:
        return False
    else:
        return True
    
    
