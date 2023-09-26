import hashlib
from user_page_functions.user_session import remember_me

def login(user_database, username,password):
    #handling username
    break_function = False
    username_list = user_database['username'].tolist()
    while username not in username_list:
        if username == "e":
            break_function = True
            print("Returning to login / register page...")
            break
        username = input("The username doesn't exists, please type it again, else exit by typing 'e': ")
    
    if break_function: return False #ends the function if breakfunction is true

    #handling password
    username_index = username_list.index(username)
    password_to_match = user_database.iloc[username_index,1]
    password = hashlib.sha256(password.encode()).hexdigest() #hashing to store password securely
    while password != password_to_match:
        password = input("The password doesn't match, please type it again, else exit by typing 'e': ")
        password = hashlib.sha256(password.encode()).hexdigest()  
        if password == hashlib.sha256('e'.encode()).hexdigest(): #this is basically if user inputs e
            break_function = True
            break
    if break_function: 
        print("Returning to login / register page...")
        return False
    print("Welcome",user_database.iloc[username_index,2])
    
    # asks the user if they want their login details to be remembered
    remember_login = input("Do you want us to remember your login details?(y/n) ")
    while remember_login not in ["y","Y","n","N"]:
        remember_login = input("Sorry I do not understand you, please input y or n only. Do you want us to remember your login details?(y/n) ")
    
    if remember_login == "y" or remember_login == "Y":
        remember_me(username)
    else:
        print("Okay, we will not remember your login details.")
                
    return username
    
