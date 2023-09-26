import hashlib
import re
import pandas as pd
import random
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from user_page_functions.login import login

def register(user_database,username,password,name,email):
    #ensure username is unique and is valid
    username_list = user_database['username'].tolist()
    while (username in username_list) or (len(username)<4):
        if len(username)<4: 
            username = input("The username must be more than 4 characters. Please input a new username: ")
        if username in username_list:
            username = input("The username already exists, please choose input a new username: ")
    
    #ensure password is strong enough and hashes the password before storing it
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$"
    mat = re.search(re.compile(reg), password)
    password_is_valid = True if mat else False
    while password_is_valid == False:
        password = input ("Password is too weak! Please input a password that is at least 8 characters long with alphanumerical characters that have a mix of upper and lower cases, and any special characters: ")
        mat = re.search(re.compile(reg), password)
        password_is_valid = True if mat else False

    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    email_list = user_database['email'].tolist()
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    valid_email = True if(re.fullmatch(email_regex, email)) else False
    
    while True:
        if (email in email_list)==False and valid_email == True:
            break
        if email in email_list:
            email = input("The email already exists. Please input a new email: ")
        if valid_email==False:
            email = input("The email format is invalid. Please input a new email: ")
        valid_email = True if(re.fullmatch(email_regex, email)) else False

    print("Please verify your e-mail by entering the OTP that will be sent to your registered e-mail.")
    print("Please note that your account will not be created if you fail to enter in the correct OTP")

    
    OTP = random.randrange(000000,999999,1)
    
    mail_content = mail_content = """ \
    <html>
        <head></head>
        <body>
    Hello {:}, <br>
    <br>
    <b>{:d}</b> is your one-time passcode (OTP) for the Money Managing app.<br>
    Please copy and paste or enter the code manually when prompted in the App to verify your account.<br>
    The code was requested from the Money Managing App on the device.<br>
    It will be valid for 4 hours.<br>
    <br>
    Please note that your account will not be created if you fail to enter the correct OTP. <br>
    <br>
    Enjoy the Money Managing App!<br>
    <br>   
    Money Managing App Team 
     </body>
    </html>
    """.format(name,OTP)
    
    
    #The mail addresses and password
    sender_address = 'ab0403python@gmail.com'
    sender_pass = 'hihi123@'
    receiver_address = email
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'OTP for Registration.'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'html'))
    try:
        #Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        print("Sending you the OTP, please wait....")
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
    except: #if client is not connected to the internet, there will be an error. We then return to end the function
        print("You have failed to register.")    
        print("We are unable to send you the OTP because you are not connected to the internet. Please connect to the internet and try again")
        return
    
    OTP=str(OTP)
    inputted_OTP = input("what is the OTP?: ")
    
    while inputted_OTP != OTP :
            inputted_OTP = input("what is the OTP? Else type e to exit registration: ")
            if inputted_OTP =="e":
                print("You have failed to register because you did not enter the correct OTP. Please try again.")
                return # breaks the function if the user fails to enter the correct OTP
        
    #if user enters the correct OTP and verifies the e-mail, we save the data to our DB
    user_credentials = [username,hashed_password,name,email]
    new_row = pd.Series(user_credentials, index = user_database.columns)
    user_database = user_database.append(new_row,ignore_index=True)
    user_database.to_csv("database/user_database.csv",index = False)
    
    #creates a .csv file for the user
    expense_data = pd.DataFrame([],columns=["Date"])
    expense_data.to_csv("database/individual_data/"+username+".csv", index=False)
    print(f"Hey {name}, you have successfully registered!")
    logged_in_status = login(user_database, username,password)  #import the login function; returns true if logged in (i.e. succesfully register)
    return logged_in_status
    