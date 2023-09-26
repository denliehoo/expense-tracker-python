import pandas as pd
from helper_functions.get_date import get_date 
from helper_functions.page_break import page_break
from datetime import datetime
import calendar

def view_expenses(username):
    print("Viewing Expenses")
    expense_data=pd.read_csv("database/individual_data/"+username+".csv", parse_dates=["Date"], index_col = "Date")
    pd.set_option("display.max_rows", None, "display.max_columns", None)                        

    if expense_data.shape[0] == 0:
            print("You have no expenses yet!")
            return

    while True:          
        action = input("1=View most recent \n2=View all \n3=View for a given year \
                       \n4=View for a given month and year \n5=View for a given period \
                           \ne=Exit view expenses \nWhat do you want to do?: ")
        page_break()
        
        if action =="1": # view most recent
            print("These are your most recent expenses")
            print(expense_data.tail())
            return
        
        elif action =="2": #view all
            print("These are all your transactions")
            print(expense_data)
            if expense_data.shape[0] >30: 
                print("Your transactions are as per above")
            return
        
        
        elif action =="3": #given year
            year=input("What year?: ")
            while year.isdigit() == False:
                year=input("What year? Please input numbers only: ")
            expense_data=pd.read_csv("database/individual_data/"+username+".csv")
            filtered_df = expense_data.loc[(expense_data['Date'] >= year+'-01-01') & (expense_data['Date'] <= year+'-09-31')]
            if filtered_df.shape[0]==0:
                print("There are no expenses for year "+year)
            else:
                print((filtered_df).to_string(index=False))
                if filtered_df.shape[0] >30: 
                    print("Your transactions are as per above")
            return

            
        elif action =="4": #given month and year
            print("Viewing expenses for a given month for a given year")
            month_values = {'Jan' : 1, 'January' : 1,
                            'Feb' : 2 , 'February' : 2, 
                            'Mar' : 3 , 'March' : 3, 
                            'Apr' : 4 , 'April' : 4, 
                            'May' : 5 , 'May' : 5, 
                            'Jun' : 6 , 'June' : 6, 
                            'Jul' : 7 , 'July' : 7, 
                            'Aug' : 8 , 'August' : 8, 
                            'Sep' : 9 , 'September' : 9, 
                            'Oct' : 10 , 'October' : 10,
                            'Nov' : 11 , 'November' : 11,
                            'Dec' : 12 , 'December' : 12}
            month_list = list(month_values.keys())
            year = input("What year?: ")
            while year.isdigit() == False:
                year=input("What year? Please input numbers only: ")           
            month_name = input("What month?: ").lower().capitalize()
            
            while month_name not in month_list:
                month_name = input("You have entered an invalid month, please type the month again (e.g. jan,feb,mar): ").lower().capitalize()
            month = month_values[month_name]
  
            end_date_day = calendar.monthrange(datetime(int(year), month, 1).year, datetime(int(year), month, 1).month)[1]
            end_date = datetime(int(year),month,end_date_day).strftime("%Y-%m-%d")
            start_date = datetime(int(year),month,1).strftime("%Y-%m-%d")
            expense_data=pd.read_csv("database/individual_data/"+username+".csv")
            filtered_df = expense_data.loc[(expense_data['Date'] >= start_date) & (expense_data['Date'] <= end_date)]
            if filtered_df.shape[0]==0:
                print(f"There are no expenses for {month_name} {year}")
            else:
                print((filtered_df).to_string(index=False))
                if filtered_df.shape[0] >20: 
                    print("Your transactions are as per above")
            return            
            
        
        elif action =="5": #given range
            print("Viewing expenses within a certain period. What are the two dates?")
            start_date=get_date("What is the start date in yyyy-mm-dd format?: ")
            end_date=get_date("What is the end date in yyyy-mm-dd format? Alternative, type 't' to get today's date: ")
            expense_data=pd.read_csv("database/individual_data/"+username+".csv")
            filtered_df = expense_data.loc[(expense_data['Date'] >= start_date) & (expense_data['Date'] <= end_date)]
            if filtered_df.shape[0]==0:
                print(f"There are no expenses between {start_date} & {end_date}")
            else:
                print((filtered_df).to_string(index=False))
                if filtered_df.shape[0] >20: 
                    print("Your transactions are as per above")            
            return
        
        elif action =="e":
            print("Exiting view expenses")
            return
        
        else:
            print("Sorry, I do not understand")
            page_break()

         
    
    

