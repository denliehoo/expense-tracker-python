#note that all file related stuff are happening w.r.t this app.py location

#useful information
#Test account:   username = testing   password = testingPassword1!

#df = pd.read_csv("database/individual_data/testing.csv", parse_dates=["Date"]) #parseDate; hence the date becomes 'pandas._libs.tslibs.timestamps.Timestamp' instead of 'str'
# can use the above and bbelow for analysis for graphs
# df = pd.read_csv("database/individual_data/testing.csv", parse_dates=["Date"], index_col = "Date") #changes the column to Date (this also changes the shape)
# df = df.sort_values(by="Date",ascending=False) #sorts by a column in reverse (descending) order
# df = df.sort_values(by="Date") #sorts by a column in ascending order

# date_values = df['Date'].tolist() #gets the value of a column and place it into a list
# row_index = date_values.index(expense_date) #gets the index of the row by giving the item

# category_values = list(df.columns.values) #get the values of the column headers and place it into a list

# changing the values of an indivudal item in the dataframe (increaseing / decrease)
# note that row_index is actually the value of that column; in this case, because our column is the index (0,1,2) we are using the index for .loc
# however, if we use the Date as the column instead (i.e. read_csv.... index_col="Date"), then we can actually do df.loc[row_name, col_name]
    # ^^ e.g. df.loc["2021-01-02", "Books"]    *note if implement this, need change all the values of the add_expense.py because using date as col instead of index changes the shape
# df.loc[row_index,col_name] += amount_to_add  #adds the amount to an exisiting value (or can do - also if needed)
# df.loc[row_index,col_name] = xxx   #just changes the value e.g. df.loc[1,'Bills'] = 100
# will need to save df at the end (.to_csv)


import pandas as pd
from manage_expenses_functions.add_expense import add_expense
from user_page_functions.login import login
from user_page_functions.register import register
from helper_functions.page_break import page_break #looks in the helper_functions folder and import the page_break function
from helper_functions.get_date import get_date #use get_date to request the date; e.g. expense_date = get_date()




#***comment / uncomment starts here***
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
        logged_in = login(user_database, username,password) #login returns the username (truthy) if logged in successfully
        username = logged_in 
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
#***comment/uncomment ends here****

#quick start guide: uncomment the bottom four lines after the next, comment the top lines (except for the imports). Unindent bottom part
#add back login guide: comment the bottom four lines, uncomment the top lines. Indent the bottom part
# end_app = False
# logged_in=True
# username = "testing" #or edit accordingly to whichever username
# user_database = pd.read_csv("database/user_database.csv")

#start of the functionalities
    while logged_in: # do logged_in == False to end this loop
        expense_data=pd.read_csv("database/individual_data/"+username+".csv") 
        page_break()
        print("Expense Tracking Application")
        application_action = input("1=manage expense \n2=analyze expenses \n.... \nanything else = logout \nWhat do you want to do?: ")
        
        
        if application_action == "1": #manage expense (create,read,update,delete)
            within_manage_expenses = True
            while within_manage_expenses == True:
                expense_data=pd.read_csv("database/individual_data/"+username+".csv")
                page_break()
                print("Manage Expenses")
                manage_expense_action=input("1=create expense \n2=view expenses \n3=updates expense \n4=delete expense \nanything else = leave managing expense \nWhat do you want to do?: ")
                if manage_expense_action =="1":
                    page_break()
                    print("Creating new expense...")
                    category_values = list(expense_data.columns.values)
                    expense_category_input_message = f"These are your current categories: {', '.join([n for n in category_values])[5:]} \nWhat category is it under?: " if len(category_values)>1 else "What category is it under?: "
                    expense_category = input(expense_category_input_message)
                    #expense_date = input("What date is it in dd-mmm-yy?: ") #eventually do regex on this
                    expense_date = get_date()
                    expense_amount = float(input("How much is the expense?: ")) #need do error handling for this
                    add_expense(username,expense_data,expense_category,expense_date, expense_amount)

                elif manage_expense_action =="2": #view
                    print(expense_data) #make it look nicer; can use this function for application_action == 2 under view also
                    #code for view
                elif manage_expense_action =="3": #update
                    #ask for what date and category and amount
                    pass
                    #code for update
                elif manage_expense_action =="4": #delete
                    #ask for what date and category and amount
                    pass
                    #code for delete
                else: 
                    print("Leaving manage expenses...")
                    within_manage_expenses=False
        
        elif application_action =="2": #analyze expenses (view charts, etc); perform more actions
            #code for action 2
            print(expense_data) #do something more meaningful with this
            
        elif application_action=="3": #something
            #code for action 3
            pass
        
        else: #any other input = log outand end app
            logged_in=False
            end_app =True
            print(f"You have logged out! \nGoodbye {username}")



# #***for testing parts without logging in; uncommmented bottom to use***
# username="testing" #or whichever dataset its called
# expense_data=pd.read_csv("database/individual_data/"+username+".csv") 
# user_database = pd.read_csv("database/user_database.csv")
# ###*** do your code here***

