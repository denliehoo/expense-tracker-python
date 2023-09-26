def get_amount():
    key = False
    while key == False:
        try:
            expense_amount = float(input("What is the expense amount? "))
            
            if expense_amount>0: # positive check
                key = True 
                            
            if key == False:
                print('Please enter a valid positive amount.')
            
            if key == True:
                return round(expense_amount,2) # 2d.p
            
        except ValueError:
            print('Please enter a valid positive amount.') # numerical check