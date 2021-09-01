#login


# username = input("What is your username?: ")
# password = input("What is your password?: ")

#maybe can do something like if login_status = login() which returns True or False. Then if true, continue on to actions
#hint: password convention here is usually username+Password1! e.g. if user name is test then password is testPassword1!
import hashlib
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
    return username
    
