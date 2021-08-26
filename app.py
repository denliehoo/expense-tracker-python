import pandas as pd
from manage_expenses_functions.add_expense import add_expense
from user_page_functions.login import login
from user_page_functions.register import register
from helper_functions.page_break import page_break #looks in the helper_functions folder and import the page_break function
from helper_functions.get_date import get_date #use get_date to request the date; e.g. expense_date = get_date()
#note that all file related stuff are happening w.r.t this app.py location

#Test account:   username = testing   password = testingPassword1!

end_app = False
while end_app == False:
    page_break()
    print("Login / Register Page")
    login_or_reg = input("1=login \n2=register \nanything else = quit application \nWhat would you like to do?: ")
    page_break()
    logged_in = False
    if login_or_reg == "1":
        print("You are about to login")
        username = input("What is your username?: ")
        password = input("What is your password?: ")
        user_database = pd.read_csv("database/user_database.csv")
        logged_in = login(user_database, username,password) #login returns true if logged in successfully
    elif login_or_reg =="2":
        print("You are registering")
        username = input("What is your username you want to register as?: ")
        password = input("What is your password you want to register as?: ")        
        name = input("What is your name?")
        user_database = pd.read_csv("database/user_database.csv")
        logged_in = register(user_database,username,password,name) #we auto log in for them after registering; register also returns true or false
    else:
        print("You have ended the application")
        end_app=True
        
    #start of the functionalities
    while logged_in==True: # do logged_out == True to end this loop
        expense_data=pd.read_csv("database/individual_data/"+username+".csv") 
        page_break()
        print("Expense Tracking Application")
        application_action = input("1=manage expense \n2=analyze expenses \n.... \nanything else = logout \nWhat do you want to do?: ")
        page_break()
        
        
        if application_action == "1": #manage expense (create,read,update,delete)
            within_manage_expenses = True
            while within_manage_expenses == True:
                expense_data=pd.read_csv("database/individual_data/"+username+".csv")
                page_break()
                print("Manage Expenses")
                manage_expense_action=input("1=create expense \n2=view expenses \n3=updates expense \n4=delete expense \nanything else = leave managing expense \nWhat do you want to do?: ")
                if manage_expense_action =="1":
                    expense_category = input("What category is it under?: ")
                    #expense_date = input("What date is it in dd-mmm-yy?: ") #eventually do regex on this
                    expense_date = get_date()
                    expense_amount = float(input("How much is the expense?: ")) #need do error handling for this
                    add_expense(username,expense_data,expense_category,expense_date, expense_amount)
                    #expense_data.to_csv("database/individual_data/"+username+".csv",index=False)
                elif manage_expense_action =="2": #view
                    print(expense_data) #make it look nicer; can use this function for application_action == 2 under view also
                    #code
                elif manage_expense_action =="3": #update
                    #ask for what date and category and amount
                    pass
                    #code
                elif manage_expense_action =="4": #delete
                    #ask for what date and category and amount
                    pass
                    #code
                else: 
                    print("Leaving manage expenses...")
                    within_manage_expenses=False
        
        elif application_action =="2": #analyze expenses (view charts, etc); perform more actions
            print(expense_data) #do something more meaningful with this
        
        elif application_action=="3": #something
            pass
        else:
            logged_in=False
            end_app =True
            print(f"You have logged out! \nGoodbye {username}")


# #***for testing parts without logging in; uncommmented bottom to use***
# username="testing" #or whichever dataset its called
# expense_data=pd.read_csv("database/individual_data/"+username+".csv") 
# user_database = pd.read_csv("database/user_database.csv")
# ###*** do your code here***

