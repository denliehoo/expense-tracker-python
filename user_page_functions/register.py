# registering ; will need to make a new .csv for the new user and add them to the user database
import hashlib
import re
import pandas as pd
from user_page_functions.login import login
#username = "hello2" #ensure username & password longer than certain number of char also; password maybe do regex also
#password = "hello2password"
#name = "Hello World" 


def register(user_database,username,password,name):
    #ensure username is unique and is valid
    username_list = user_database['username'].tolist()
    while (username in username_list) or (len(username)<4):
        if len(username)<4: 
            username = input("The username must be more than 6 characters. Please input a new username: ")
        if username in username_list:
            username = input("The username already exists, please choose input a new username: ")
    
    #ensure password is strong enough and hashes the password before storing it
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$"
    mat = re.search(re.compile(reg), password)
    password_is_valid = True if mat else False
    while password_is_valid == False:
        password = input ("Password is too weak! Please ensure input a password that is at least 8 characters long with alphanumerical characters that have a mix of upper and lower cases, and any special characters: ")
        mat = re.search(re.compile(reg), password)
        password_is_valid = True if mat else False

    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    user_credentials = [username,hashed_password,name]
    a_series = pd.Series(user_credentials, index = user_database.columns)
    user_database = user_database.append(a_series,ignore_index=True)
    
    user_database.to_csv("database/user_database.csv",index = False)
    expense_data = pd.DataFrame([],columns=["Date"])
    expense_data.to_csv("database/individual_data/"+username+".csv", index=False)
    print(f"Hey {name}, you have successfully registered!")
    logged_in_status = login(user_database, username,password)  #import the login function; returns true if logged in (i.e. succesfully register)
    return logged_in_status
    

