#Test account:   username = testing   password = testingPassword1!

import pandas as pd
import matplotlib.pyplot as plt

from manage_expenses_functions.add_expense import add_expense
from manage_expenses_functions.view_expenses import view_expenses
from manage_expenses_functions.update_expense import update_expense
from manage_expenses_functions.delete_expense import delete_expense

from user_page_functions.login import login
from user_page_functions.register import register
from user_page_functions.forgot_password import forgot_password

from user_page_functions.user_session import forget_me
from user_page_functions.user_session import check_if_remembered
from user_page_functions.user_session import remember_me

from analyze_expenses_functions.pie_chart_percentage import pie_chart_percentage
from analyze_expenses_functions.pie_chart_numerical import pie_chart_numerical
from analyze_expenses_functions.comparison_graph import comparison_graph
from analyze_expenses_functions.total_expenses_graph import total_expenses_graph

from helper_functions.page_break import page_break #looks in the helper_functions folder and import the page_break function


end_app = False
while end_app == False:
    username_remembered = check_if_remembered() #returns false if nothing remembered, returns the username if something is remembered
    if username_remembered == False: #if no username is remembered or if username remembered has expired due to login time being more than 1 day ago
        page_break()
        print("Login / Register Page")
        login_or_reg = input("1=login \n2=register \n3=forgot password \ne=quit application \nWhat would you like to do?: ")
        page_break()
        logged_in = False
        if login_or_reg == "1": # login
            print("You are about to login")
            username = input("What is your username?: ")
            password = input("What is your password?: ")
            user_database = pd.read_csv("database/user_database.csv")
            logged_in = login(user_database,username,password) #login returns the username (truthy) if logged in successfully
            username = logged_in 
            
        elif login_or_reg =="2": # register
            print("You are registering")
            username = input("What is your username you want to register as?: ")
            password = input("What is your password you want to register as?: ")    
            name = input("What is your name?: ")
            email = input("What is your email?: ")
            user_database = pd.read_csv("database/user_database.csv")
            logged_in = register(user_database,username,password,name,email) #we auto log in for them after registering; register also returns true or false
            user_database = pd.read_csv("database/user_database.csv") #after register, the data hence we read the file again
            
        elif login_or_reg=="3": # forgot password
            print("You are about to reset your password")
            email = input("Please enter your registered email: ")
            forgot_password(email)
            
        elif login_or_reg=="e": # ends the application
            print("You have ended the application")
            end_app=True
        
        else:
            print("Sorry, I do not understand")
    else: #if there is already a username remember in the user session, we automatically log the user in
        logged_in = username_remembered
        username = username_remembered
        user_database = pd.read_csv("database/user_database.csv")
        

    #start of the functionalities: manage expenses / analyze expenses / reset password
    while logged_in: # do logged_in == False to end this loop
        expense_data=pd.read_csv("database/individual_data/"+username+".csv") 
        page_break()
        print("Expense Tracking Application")
        application_action = input("1=manage expense \n2=analyze expenses \n3=change password \ne=logout \nWhat do you want to do?: ")

        if application_action == "1": #manage expense (create,read,update,delete)
            within_manage_expenses = True
            while within_manage_expenses == True:
                page_break()
                print("Manage Expenses")
                manage_expense_action=input("1=create expense \n2=view expenses \n3=update expense \n4=delete expense \
                                            \ne=leave managing expense \nWhat do you want to do?: ")
                if manage_expense_action =="1":
                    page_break()
                    print("Creating new expense...")
                    add_expense(username)

                elif manage_expense_action =="2": #view
                    page_break()
                    view_expenses(username) #user will have 5 options inside the view function
                  
                elif manage_expense_action =="3": #update
                    page_break()
                    print('Updating Expense')
                    update_expense(username)
                    
                elif manage_expense_action =="4": #delete
                    page_break()
                    print('Deleting Expense')
                    delete_expense(username)
            
                elif manage_expense_action =="e":
                    print("Leaving manage expenses...")
                    within_manage_expenses=False
                    
                else: 
                    print("Sorry, I do not understand")
                    
        #analyze expenses            
        elif application_action =="2": 
            expense_data = pd.read_csv ("database/individual_data/"+username+".csv")
            if not expense_data.empty:
                within_analyze_expenses = True
                while within_analyze_expenses == True:
                    page_break()
                    print("Analyze Expenses")
                    analyze_expense_action=input("1=view expenses for each category within a period \n2=compare spending of 2 categories within a period \
                                                 \n3=view total expenses within a period \ne=leave analyze expenses \nWhat do you want to do?: ")
                    
                    if analyze_expense_action =="1": #view expenses for each category within a period
                        page_break()
                        analyze_expense_action1 = input("Would you like to view expenses as\
                              \n1=percentages \n2=numerical totals \nPlease select: ")
                        page_break()
                        if analyze_expense_action1 =="1": #view as percentages
                            pie_chart_percentage(username)
                            plt.show() 
                            
                        elif analyze_expense_action1 =="2":#view as numeric totals
                            pie_chart_numerical(username)
                            plt.show() 
                            
                        elif analyze_expense_action1 =="e":
                            print("Leaving analyze expenses...")
                            within_analyze_expenses=False   
                            
                        else: 
                            print("Sorry, I do not understand")
    
                    elif analyze_expense_action =="2": #compare spending of 2 categories within a period
                        page_break()
                        comparison_graph(username)
                      
                    elif analyze_expense_action =="3": #view total expenses within a period
                        page_break()
                        total_expenses_graph(username)
                
                    elif analyze_expense_action =="e":
                        print("Leaving analyze expenses...")
                        within_analyze_expenses=False
                        
                    else: 
                        print("Sorry, I do not understand")
            else:
                print('''Insufficient data. Please add data under "manage expenses".''')
                within_analyze_expenses=False
                     
        #change password    
        elif application_action=="3": 
            username_list = user_database['username'].tolist()
            row_index = username_list.index(username)
            email = user_database.loc[row_index,'email']
            print("You are about to reset your password")
            forgot_password(email)
        
        elif application_action=="e": #logouts and exits the application
            logged_in=False
            end_app =True
            username_list = user_database['username'].tolist()
            row_index = username_list.index(username)
            name = user_database.loc[row_index,'name']  
            if check_if_remembered() == username: #only if there is a user session remembered will this be prompted
                still_remember = input("Do you want us to continue remembering your login details? (y/n) ")
                while still_remember not in ["Y",'y',"N",'n']:
                    still_remember = input("Sorry, I do not understand you, please input y or n only. Do you want us to continue remembering your login details? (y/n)")
                if still_remember == "Y" or still_remember == 'y':
                    remember_me(username) #extends the user session
                else:
                    forget_me() #forgets the user session
                    print("Okay, we will not remember your login details.")
        
            print(f"You have ended the application! \nGoodbye {name}")

        
        else: 
            print("Sorry, I do not understand")
            


