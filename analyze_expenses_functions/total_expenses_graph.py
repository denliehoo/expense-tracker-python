import pandas as pd
import matplotlib.pyplot as plt

from helper_functions.page_break import page_break
from helper_functions.get_date import get_date

def total_expenses_graph(username):
    print("Viewing total expenses within a period...\
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
    # Filter data between two dates
    filtered_df = expense_data.loc[(expense_data['Date'] >= start_date) & (expense_data['Date'] <= end_date)] 
    
    df2 = filtered_df.assign(Total_Expenses = list(filtered_df.sum(axis=1)))
    #add new column containing the sum of expenses per date
    
    data = (df2.filter(regex='Total_Expenses'))
    data_count = data.count()
    
    if data_count[0] >= 2: #if enough data points, plot graph
        df2.plot('Date', 'Total_Expenses', figsize=(20, 15))
        plt.legend(title=r'$\bf{TotalExpenses}$',fontsize=20, title_fontsize = 25, loc="upper right")
        plt.xlabel('Date', size = 20)
        plt.ylabel('Amount ($)', size = 20)
        plt.xticks(size = 18)
        plt.yticks(size = 18)    
    
        plt.show()    
        
    else:
        print('''Insufficient data. Please enter other date ranges or add more data under "manage expenses".''')  
