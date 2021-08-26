import pandas as pd
from manage_expenses_functions.add_category import add_category
def add_expense(username,expense_data,expense_category,expense_date, expense_amount):
    category_values = list(expense_data.columns.values) # puts the the headers (i.e. the categories) into a list
    break_function = False
    y_n_values =["y","Y","n","N"]
    while expense_category == "Date":
        expense_category = input("You are not allowed to use 'Date' as a category. Please choose another category: ")
    
    while expense_category not in category_values:
      input_helper = f"Did you make a typo? These are your current categories: {', '.join([n for n in category_values])}" if len(category_values)>1 else "You currently have no categories"
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
            expense_category = input("Type in the new category name: ")
            while expense_category == "Date":
                expense_category = input("You are not allowed to use 'Date' as a category. Please choose another category: ")
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
          elif add_diff_cat_res=="n" or add_diff_cat_res=="N":
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
        initial_amount = float(expense_data.iloc[row_index,column_index]) #have to convery the numpyin64 object to a float
        col_name= category_values[column_index]
        expense_data.loc[row_index,col_name] = (expense_amount + initial_amount)  #adds the amount
        print("Added to the current row for the date")

    else: #i.e. if the date doesn't exist in the date column, then we'll need to make a new row for it and add the data
        new_row_data = [expense_date]
        for i in range(1,total_columns):
            if i==column_index:
                new_row_data.append(expense_amount)
            else:
                new_row_data.append(0)
        a_series = pd.Series(new_row_data, index = expense_data.columns)
        expense_data = expense_data.append(a_series,ignore_index=True)
    
    expense_data.to_csv("database/individual_data/"+username+".csv",index=False) #saves to the csv
        




# import pandas as pd
# from add_category import add_category
# def add_expense(username,expense_data,expense_category,expense_date, expense_amount):
#     category_values = list(expense_data.columns.values) # puts the the headers (i.e. the categories) into a list
#     break_function = False
#     while expense_category not in category_values:
#       input_helper = f"Did you make a typo? These are your current categories: {', '.join([n for n in category_values])}" if len(category_values)>0 else "You currently have no categories"
#       add_cat_res = input(f"The category doesn't exit. \n{input_helper} \nAdd the expense to a new category '{expense_category}'?(y/n) ")
#       while add_cat_res not in ['y',"Y","n","N"]:
#           add_cat_res = input(f"Sorry, I do not understand you. Please type 'y' or 'n'.\nThe category doesn't exit. \n{input_helper} \nAdd the expense to a new category '{expense_category}'?(y/n) ")
#       if add_cat_res == "y" or add_cat_res=="Y":
#           add_category(username,expense_data,expense_category)
#           category_values.append(expense_category)
#           break
#       elif add_cat_res == "n" or add_cat_res=="N":
#           print("The category wasn't added.")
#           add_diff_cat_res = input('Would you like to add the expense to a different category instead? (y/n) ')
#           while add_diff_cat_res not in ['y',"Y","n","N"]:
#             add_diff_cat_res = input("Sorry, I do not understand you. Please type 'y' or 'n'.\nWould you like to add the expense to a different category instead? (y/n) ")
#           if add_diff_cat_res == "y" or add_diff_cat_res == "Y":
#             expense_category = input("Type in the new category name: ")
#             if expense_category in category_values:
#                 print("That category already exists. Adding it to the existing category") #breaks and skips to add it. 
#                 break
#             add_category(username,expense_data,expense_category)
#             category_values.append(expense_category)
#             break
#           elif add_diff_cat_res=="n" or add_diff_cat_res=="N":
#             print("No category or expense has been added.")
#             break_function = True
#             break

#     if break_function == True:
#         print("Leaving the add expense section...")
#         return
    
#     column_index = expense_data.columns.get_loc(expense_category)
#     total_columns=expense_data.shape[1] #data.shape returns [total rows,total columns]
#     date_values = expense_data['Date'].tolist() #puts the date column into a list

#     if expense_date in date_values: #i.e. if the date is an existing one in the date column, then we find the row and column and add accordingly
#         row_index = date_values.index(expense_date)
#         initial_amount = float(expense_data.iloc[row_index,column_index])
#         col_name= category_values[column_index]
#         expense_data.loc[row_index,col_name] = (expense_amount + initial_amount)  #adds the amount
#         print("Added to the current row for the date")

#     else: #i.e. if the date doesn't exist in the date column, then we'll need to make a new row for it and add the data
#         new_row_data = [expense_date]
#         for i in range(1,total_columns):
#             if i==column_index:
#                 new_row_data.append(expense_amount)
#             else:
#                 new_row_data.append(0)
#         a_series = pd.Series(new_row_data, index = expense_data.columns)
#         expense_data = expense_data.append(a_series,ignore_index=True)
    
#     expense_data.to_csv("database/individual_data/"+username+".csv",index=False) #saves to the csv
        

