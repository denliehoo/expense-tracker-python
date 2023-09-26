import datetime
import pandas as pd


#use w because we want to re-write the file contents
def forget_me():
    with open('database/local_data.txt',"w") as f:
        f.write("0")
        

def remember_me(username): #remember the user for an hour
    with open('database/local_data.txt',"w") as f:
        current = datetime.datetime.now()    
        hours_added = datetime.timedelta(hours=24) #adds an hour to the current time
        forget_me_date_str = (current + hours_added).strftime("%Y-%m-%d %H:%M:%S")
        data = username+","+forget_me_date_str
        f.write(data)

def check_if_remembered():
    with open('database/local_data.txt',"r+") as f:
        data = f.read()
        if data == "0": # 0 in the text file means there is no data in the session
            return False
        else:
            data_list = data.split(',')
            username = data_list[0]
            forget_me_date_str = data_list[1]
            forget_me_date_obj = datetime.datetime.strptime(forget_me_date_str, "%Y-%m-%d %H:%M:%S")
            current = datetime.datetime.now() 
            if current < forget_me_date_obj:
                user_database = pd.read_csv("database/user_database.csv")
                username_list = user_database['username'].tolist()
                row_index = username_list.index(username)
                name = user_database.loc[row_index,'name']  
                print(f"Welcome back {name}!")
                return username
            else:
                forget_me() #re-writes the file to just "0" using the function above
                print("Your session has expired because it has been more than 1 day since you logged in. Please login again.")
                return False
    
        
        



