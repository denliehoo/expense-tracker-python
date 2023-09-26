import pandas as pd
from helper_functions.get_date import get_date 
from helper_functions.check_existing_date_and_category import check_existing_date_and_category
from helper_functions.get_amount import get_amount

    
def update_expense(username):
    expense_data=pd.read_csv("database/individual_data/"+username+".csv")
    if (expense_data.shape[0]) == 0:
        print("You have no expenses yet!")
        return
    
    input_date = get_date()    
    input_category = input("Please enter your category: ").capitalize()
    date_and_category_exist = check_existing_date_and_category(input_category,input_date,username)
    if date_and_category_exist == True:
        new_expense = get_amount()
        date_values = expense_data['Date'].tolist()   
        date_index = date_values.index(input_date)
        expense_data.loc[date_index,input_category]=new_expense
        expense_data.to_csv("database/individual_data/"+username+".csv",index=False)
        print("Your expense has been successfully updated.")  
        
    else:
           print("Either the date or category doesn't exist")
          





    
         
    
    

