import random
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import hashlib
import re

def forgot_password(email):    
    user_database = pd.read_csv("database/user_database.csv")
    email_list = user_database['email'].tolist()
    while email not in email_list:
        email = input("The email doesnt exist, what is your email? Else type e to exit: ")
        if email == "e":
            return
    row_index = email_list.index(email)
    name = user_database.loc[row_index,'name']   
            
    OTP = random.randrange(000000,999999,1)
     
    mail_content = mail_content = """ \
    <html>
        <head></head>
        <body>
    Hello {:}, <br>
    <br>
    <b>{:d}</b> is your one-time passcode (OTP) for the Money Managing app.<br>
    Please copy and paste or enter the code manually when prompted in the App to reset your password.<br>
    The code was requested from the Money Managing App on the device.<br>
    It will be valid for 4 hours.<br>
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
    message['Subject'] = 'OTP for resetting password.'   #The subject line
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
        print("You have failed to reset your password.")
        print("We are unable to send you the OTP because you are not connected to the internet. Please connect to the internet and try again")
        return
    
    print('Mail Sent. If you did not receive it, please check your spam mail')
    
    OTP=str(OTP)
    inputted_OTP = input("what is the OTP? ")
    
    while inputted_OTP != OTP :
            inputted_OTP = input("what is the OTP? Else type e to exit the app: ")
            if inputted_OTP =="e":
                print("You have failed to reset your password. Please try again")
                return 
   
    
    password = input("What is your new password?")
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$"
    mat = re.search(re.compile(reg), password)
    password_is_valid = True if mat else False
    while password_is_valid == False:
        password = input ("Password is too weak! Please input a password that is at least 8 characters long with alphanumerical characters that have a mix of upper and lower cases, and any special characters: ")
        mat = re.search(re.compile(reg), password)
        password_is_valid = True if mat else False

    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    user_database.loc[row_index,'password'] = hashed_password
    user_database.to_csv("database/user_database.csv",index = False)
    print("You have successfully resetted your password!")

    
    
    
    
