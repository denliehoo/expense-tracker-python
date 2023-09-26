#ensure that date is in yyyy-mm-dd format
#returns the input_date; hence we can do expense_date = get_date() in our app.py

#rationale for converting it to using datetime and back is that if the user puts in integers
# but invalid date, e.g. for month its 2 but day is 30, then they will reject because feb doesn't have 30 days, etc.
import datetime

#optional argument, if no message is inputted, fallback on the default message
def get_date(message="What is the date in yyyy-mm-dd format. Alternative, type 't' to get today's date: "): 
    input_date = ""
    while True:
        try:
            input_date = input(message)
            if input_date == "t":
                input_date =  datetime.datetime.today().strftime('%Y-%m-%d')
                break
            else:        
                input_year="" 
                input_month=""
                input_day=""
                dash_count = 0
                for char in input_date:
                    if char =="-":
                        dash_count +=1
                    else:
                        if dash_count ==0:
                            input_year +=char
                        elif dash_count ==1:
                            input_month += char
                        elif dash_count ==2:
                            input_day += char   
                input_date = datetime.datetime(int(input_year), int(input_month), int(input_day))
                input_date = input_date.strftime("%Y-%m-%d")
                break
        except:
            print("Ensure date is valid and is in yyyy-mm-dd format")
    return input_date
