# def get_date(date):
#     date_is_valid = False
#     if date_is_valid == True:
#         return date
#     elif date_is_valid == False:
#         date = input("Please input a date in dd-mmm-yy format: ")
#         return date

#ensure that date is in yyyy-mm-dd format
import datetime

def get_date():
    # yyyy-mm-dd
    # input_date = "2020-12-21"
    
    input_date = ""
    while True:
      try:
        input_date = input("What is the date? in yyyy-mm-dd: ")
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
