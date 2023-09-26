import pandas as pd
import matplotlib.pyplot as plt

from helper_functions.page_break import page_break
from helper_functions.get_date import get_date

def pie_chart_numerical(username):

    print("Viewing total expenses for each category within a period...\
          \nWhat are the start and end dates respectively?")
    while True:
        start_date = get_date("What is the start date in yyyy-mm-dd format?: ")
        end_date = get_date("What is the end date in yyyy-mm-dd format? Alternative, type 't' to get today's date: ")
        if start_date < end_date:
            break
        else:
            print("Invalid start and end dates. Start date has to be earlier than end date. Please try again.")
    page_break()
    print("Analyzing expenses from " + start_date + " to " + end_date + '...')
    
    expense_data = pd.read_csv ("database/individual_data/"+username+".csv")

    expense_data['Date'] = pd.to_datetime(expense_data['Date'], format='%Y-%m-%d') # Convert the date to datetime64
    # Filter data between two dates
    filtered_df = expense_data.loc[(expense_data['Date'] >= start_date) & (expense_data['Date'] <= end_date)]
    
    category_count = filtered_df.count()    
    
    if category_count.sum() < 1: #if not enough data points
        print('''Insufficient data. Please enter other date ranges or add more data under "manage expenses".''')
    
    else:    
        for category in (filtered_df[(filtered_df.columns.values)]):
            category = (filtered_df[(filtered_df.columns.values)[1:]]).sum()

        df = category[category != 0] #remove 0 values
       
        labels = (df.index).tolist()
           
        explode = []
        for i in labels:
            explode.append(0.1)
        
        textprops = {"fontsize":30}
        p, tx, autotexts = plt.pie(df, labels=labels, radius=4, startangle=90, autopct="1.2f", textprops=textprops,\
                shadow=True, explode=explode)
        for i, a in enumerate(autotexts):
            a.set_text("${:.2f}".format(df[i]))
        plt.legend(title=r'$\bf{Expenses}$',fontsize=25, title_fontsize = 30, loc="upper left")
        plt.show
               
  