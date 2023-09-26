import pandas as pd
import matplotlib.pyplot as plt

from helper_functions.page_break import page_break
from helper_functions.get_date import get_date 

def comparison_graph(username):
    print("Comparing expense categories within a period...\
          \nWhat are the start and end dates respectively?")
    while True:
        start_date = get_date("What is the start date in yyyy-mm-dd format?: ")
        end_date = get_date("What is the end date in yyyy-mm-dd format? Alternative, type 't' to get today's date: ")
        if start_date <= end_date:
            break
        else:
            print("Invalid start and end dates. Start date has to be earlier than end date. Please try again.")
    page_break()
    print("Analyzing expenses from " + start_date + " to " + end_date + '...')
    
    expense_data = pd.read_csv ("database/individual_data/"+username+".csv")

    expense_data['Date'] = pd.to_datetime(expense_data['Date'], format='%Y-%m-%d') # Convert the date to datetime64
    # Filter data between two dates:
    filtered_df = expense_data.loc[(expense_data['Date'] >= start_date) & (expense_data['Date'] <= end_date)] 
    category_values = list(expense_data.columns.values) # puts the headers (i.e. the categories) into a list
    category_input_message = f"These are your current categories: {', '.join([n for n in category_values])[5:]}.\
        \nPlease specify 2 categories to analyze. "if len(category_values)>1 else "You currently have no categories"
    print(category_input_message)
    while True:
        category1 = input("Enter first category: ")
        category1 = category1.capitalize()
        if category1 in category_values:
            break
        else:
            print("Invalid category. Please try again.")
            
    while True:
        category2 = input("Enter second category: ")
        category2 = category2.capitalize()
        if category2 in category_values:
            break
        else:
            print("Invalid category. Please try again.")       
    
    expense_data1 = filtered_df.filter(regex=category1+'|Date') 
    expense_data2 = filtered_df.filter(regex=category2+'|Date')
    data_count1 = expense_data1[expense_data1.columns[0]].count()  
    data_count2 = expense_data2[expense_data2.columns[0]].count()  
    # check if sufficient data points to construct graph
    
    if data_count1 <= 2 and data_count2 <= 2: #if not enough data points
        print('''Insufficient data. Please enter other date ranges or add more data under "manage expenses".''')
    # use a regex so it is easy to look for columns that contain one or more patterns

    else:
        expense_data1.plot(x = 'Date', y = category1, figsize=(20, 15), linewidth=3)
        plt.plot( 'Date', category2, data=expense_data2, marker='', color='olive', linewidth=2)
        plt.legend(title=r'$\bf{ExpenseCategories}$',fontsize=20, title_fontsize = 25, loc="upper right")
        plt.xlabel('Date', size = 20)
        plt.ylabel('Amount ($)', size = 20)
        plt.xticks(size = 18)
        plt.yticks(size = 18)
        plt.show()
