import pandas as pd
from manage_expenses_functions.add_category import add_category
from helper_functions.get_date import get_date 
from helper_functions.get_amount import get_amount



def add_expense(username):
    expense_data=pd.read_csv("database/individual_data/"+username+".csv")
    category_values = list(expense_data.columns.values) # puts the the headers (i.e. the categories) into a list
    expense_category_input_message = f"These are your current categories: {', '.join([n for n in category_values])[5:]} \
        \nWhat category is it under? If the category doesn't already exist, you can also type it here to create a new category: "\
            if len(category_values)>1 else "What category is it under?: "
    expense_category = input(expense_category_input_message).capitalize()
    expense_date = get_date()
    expense_amount = get_amount()
    
    break_function = False
    y_n_values =["y","Y","n","N"]
    while expense_category == "Date":
        expense_category = input("You are not allowed to use 'Date' as a category. Please choose another category: ").capitalize()
    
    while expense_category not in category_values:
      input_helper = f"Did you make a typo? These are your current categories: {', '.join([n for n in category_values])[5:]}" if len(category_values)>1 else "You currently have no categories"
      add_cat_res = input(f"The category doesn't exist. \n{input_helper} \nAdd the expense to a new category '{expense_category}'?(y/n) ")
      while add_cat_res not in y_n_values:
          add_cat_res = input(f"Sorry, I do not understand you. Please type 'y' or 'n'.\nThe category doesn't exit. \n{input_helper} \nAdd the expense to a new category '{expense_category}'?(y/n) ")
      if add_cat_res == "y" or add_cat_res=="Y":
          add_category(username,expense_data,expense_category)
          category_values.append(expense_category)
          break
      
      elif add_cat_res == "n" or add_cat_res=="N":
          print("The category wasn't added.")
          add_diff_cat_res = input('Would you like to add the expense to a different category instead? (y/n) ')
          while add_diff_cat_res not in y_n_values:
            add_diff_cat_res = input("Sorry, I do not understand you. Please type 'y' or 'n'.\nWould you like to add the expense to a different category instead? (y/n) ")
          if add_diff_cat_res == "y" or add_diff_cat_res == "Y":
            expense_category = input("Type in the new category name: ").capitalize()
            while expense_category == "Date":
                expense_category = input("You are not allowed to use 'Date' as a category. Please choose another category: ").capitalize()
            if expense_category in category_values:
                print("That category already exists. Adding it to the existing category") #breaks and skips to add it. 
                break
            else:
                add_new_cat_res = input(f"Creating a new category '{expense_category}' and adding the expense to it. Proceed? (y/n) ")
                while add_diff_cat_res not in y_n_values:
                    add_new_cat_res = input(f"Sorry, I do not understand you. Please type 'y' or 'n'.\nCreating a new category {expense_category} and adding the expense to it. Proceed? (y/n) ")
                if add_new_cat_res =="y" or add_new_cat_res=="Y":
                    add_category(username,expense_data,expense_category)
                    category_values.append(expense_category)
                    break
                else: #if n or N
                    break_function = True
                    break
                
          elif add_diff_cat_res=="n" or add_diff_cat_res=="N": #if user doesn't want to add expense to a new category
            break_function = True
            break

    if break_function == True:
        print("No category or expense has been added.")
        print("Leaving the add expense section...")
        return
    
    column_index = expense_data.columns.get_loc(expense_category)
    total_columns=expense_data.shape[1] #data.shape returns [total rows,total columns]
    date_values = expense_data['Date'].tolist() #puts the date column into a list

    if expense_date in date_values: #i.e. if the date is an existing one in the date column, then we find the row and column and add accordingly
        row_index = date_values.index(expense_date)
        col_name= category_values[column_index]
        expense_data.loc[row_index,col_name] += expense_amount
        print(f"Added ${expense_amount} to '{expense_category}' on {expense_date}. The total expense for '{expense_category}' on {expense_date} is now ${expense_data.loc[row_index,col_name]}")
        

    else: #i.e. if the date doesn't exist in the date column, then we'll need to make a new row for it and add the data
        new_row_data = [expense_date]
        for i in range(1,total_columns):
            if i==column_index:
                new_row_data.append(expense_amount)
            else:
                new_row_data.append(0) #to ensure it format [0,0,0,...,expense_amount,0...] where expense_amount is in the relevant column index
        
        print(f"Added ${expense_amount} to '{expense_category}' on {expense_date}. The total expense for '{expense_category}' on {expense_date} is now ${expense_amount}")
        new_row = pd.Series(new_row_data, index = expense_data.columns)
        expense_data = expense_data.append(new_row,ignore_index=True)
    
    expense_data = expense_data.sort_values(by=["Date"], ascending = True) #sorts by date before saving (lowest date first)
    expense_data.to_csv("database/individual_data/"+username+".csv",index=False) #saves to the csv

