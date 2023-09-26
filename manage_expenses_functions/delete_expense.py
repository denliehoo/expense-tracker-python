import pandas as pd
from helper_functions.get_date import get_date 
from helper_functions.check_existing_date_and_category import check_existing_date_and_category


def delete_expense(username):
    expense_data=pd.read_csv("database/individual_data/"+username+".csv")
    if (expense_data.shape[0]) == 0:
        print("You have no expenses yet!")
        return
    
    delete_action = input("1=delete an expense \n2=delete a category \ne=exit delete expenses \nWhat do you want to do?: ")
    while delete_action not in ["1","2","e"]:
        delete_action = input("1=delete an expense \n2=delete a category \ne=exit delete expenses \nWhat do you want to do?: ")
        
    
    if delete_action == "1" :   # delete an expense
        input_date = get_date()
        input_category = input("Please enter your category: ").capitalize()
        date_and_category_exist = check_existing_date_and_category(input_category,input_date,username)
        if date_and_category_exist == True:
            date_values = expense_data['Date'].tolist()
            date_index = date_values.index(input_date)
            expense_data.loc[date_index,input_category]= 0  
            print("Your expense has been successfully deleted.")
            cat_values = expense_data.iloc[date_index].tolist()[1:]      
            if sum(cat_values) == 0.0:
                expense_data.drop([date_index],inplace=True)
                print("Expenses from this date is zero, all entries from this date will be deleted.")
            expense_data.to_csv("database/individual_data/"+username+".csv",index=False)
                
        else:
               print("Either the date or category doesn't exist")
        
    elif delete_action == "2" :   # delete a category
        category_names = list(expense_data.columns.values)
        input_category_input_message = f"These are your current categories: {', '.join([n for n in category_names])[5:]} \nPlease enter our category: "
        input_category = input(input_category_input_message).capitalize()
        if input_category not in category_names:
            print("The category doesn't exist, leaving delete expenses...")
            return
        confirmation = input(f"Deleteing the category and all expenses for {input_category}. Are you sure you wish to delete it? This action cannot be reversed.  (y/n) ")
        while confirmation not in ["y","Y","n","N"]:
            confirmation = input(f"Sorry, I do not understand you, please type in y or n only. Deleteing the category and all expenses for {input_category}. Are you sure you wish to delete it? This action cannot be reversed.  (y/n) ")
        if confirmation in ["y","Y"]:
            expense_data.pop(input_category)
            expense_data.to_csv("database/individual_data/"+username+".csv",index=False)
            print("We have deleted the category!")
            return
        else:
            print("Okay, not deleting the category and expenses, leaving managing expenses...")
            return
        
    
    elif delete_action == "e" :  
        print("Leaving delete expenses")
        return 
           